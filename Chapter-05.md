# 第五天

## 视图

### 添加views
现在让我们再添加一些视图到myapp/views.py。这些视图与我们第一index，略有不同
它们有参数

````
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world, You're at myapp index")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
````

修改myapp/urls.py的path来调用这些views
````
from django.urls import path

from .  import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /myapp/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /myapp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
````
在浏览器输入"http://127.0.0.1:8000/myapp/1/"，将运行detail（）方法并显示你在URL中提供的任何ID。
尝试“http://127.0.0.1:8000/myapp/1/results/”和“http://127.0.0.1:8000/myapp/1/vote/” - 这些将显示结果和投票页面。
当有人从你的网站请求一个页面 - 比如说“http://127.0.0.1:8000/myapp/1/”时，Django将加载mysite.urls 模块(setting中的ROOT_URLCONF配置的）
它找到名为urlpatterns的变量并按顺序遍历这些模式,在'myapp/'找到匹配项后，它会去掉匹配的文本（“myapp/”），
并将剩余的文本“1/”发送到“myapp.urls” 以供进一步处理,在那里匹配'<int：question_id>/'，调用detail（）视图，如下所示：
````
detail(request=<HttpRequest object>, question_id=1)
````

question_id=1部分来自<int：question_id>。使用尖括号“捕获”部分URL并将其作为关键字参数发送到视图函数。
该字符串的：question_id>部分定义将用于标识匹配模式的名称,并且<int：部分是一个转换器，它决定了哪些模式应该匹配这部分URL路径。

### 编写有用view

每个视图负责执行以下两项操作之一：返回包含所请求页面内容的HttpResponse对象，或引发异常（如Http404）
视图可以从数据库中读取记录，可以使用模板系统，可以生产html,json,xml,zip,pdf 等等
以下是一个新的index（）视图，它显示了系统中最新的5个轮询问题，用逗号分隔：

````
from django.http import HttpResponse
# Create your views here.

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
````

但这里有一个问题：页面的设计在视图中是硬编码的。 如果你想改变页面的内容，你必须编辑这个Python代码
因此，让我们使用Django的模板系统，将python代码和页面内容分离

首先，在myapp目录中创建一个名为templates的目录。 Django将在那里寻找模板。
mysite/settings.py中的TEMPLATES设置了Django如何加载和渲染模板。默认设置模板系统为DjangoTemplates， 且'APP_DIRS': True,
按照惯例，DjangoTemplates在INSTALLED_APPS中查找“templates”子目录。
在myapp/templates 目录中创建一个目录为myapp，在myapp/templates/myapp 中创建一个文件叫index.html

````
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

````

现在让我们更新我们的myapp/views.py中的索引视图以使用模板：

````
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('myapp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
````

该代码加载名为myapp/index.html的模板并将其传递给上下文，上下文是一个将模板变量名称映射到Python对象的字典

快捷方式 render()
````
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'myapp/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
````

render() 函数将请求对象作为第一个参数，将模板名称作为第二个参数，将字典作为其可选的第三个参数。 
它返回给定上下文呈现给定模板的HttpResponse对象。
