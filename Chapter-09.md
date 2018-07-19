# 第十天

## 创建主页

我们现在可以添加代码来显示我们的第一个完整页面 -  LocalLibrary 网站的主页，显示每个模型类型有多少条记录，并提供我们其他页面的侧边栏导航链接。我们将编写基本URL映射和视图，从数据库获取记录以及使用模板展示

现在我们已经定义了我们的模型，并创建了一些数据，现在是编写代码以向用户呈现该信息的时候了。我们需要做的第一件事是确定我们希望能够在我们的页面中显示哪些信息，然后为返回这些资源定义适当的URL。那么我们将需要创建一个url映射器，视图和模板来显示这些页面。

以下图表提供了处理HTTP请求/响应时需要实现的数据和事情的主要流程。我们已经创建了这个模型，我们需要创建的主要内容是：

+ URL映射-根据匹配的URL转到相应的View功能。
+ View 函数从模型 获取请求的数据，创建一个显示数据的HTML页面，并将其返回给用户在浏览器查看。
+ 模板用来渲染view的数据

![img](./Chapter-09-code/basic-django.png)

### 定义资源URL
我们要为该网站提供一个登录页，以及显示书和作者的列表和详细视图的页面。
下面这些URL 是我们页面需要的
+ catalog/ — 主页
+ catalog/books/ — 书单页 列表视图
+ catalog/authors/ — 作者页 列表视图
+ catalog/book/<id> —详细视图。如下例子 ／catalog/book/3，id为3的书的详情
+ catalog/author/<id> — 详细视图。如下例子 /catalog/author/11，id为11的作者详情

### 创建主页
打开locallibrary/catalog/urls.py 添加一下内容

```
urlpatterns = [
    path('', views.index, name='index'),
]
```

path()函数定义了一个URL模式（在这种情况下是一个空字符串：''），在匹配到模式时将调用的视图函数（views.index - views.py中名为index()的函数）。

此path()函数还指定name参数，该参数唯一标识此特定URL映射。以使用此name“反转”映射器 - 动态创建指向映射器的资源的URL
例如，有了这个，我们现在可以通过在模板中创建以下链接从任何其他页面链接到我们的主页
```
<a href="{% url 'index' %}">Home</a>
```

我们可以对上面的链接进行硬编码（例如`<a href="/catalog/">主页</a>`），但如果我们更改了主页的模式（例如更改为/ catalog/index），模板将不再正确链接。使用反向url映射更加灵活和强大！

### View (基于函数)

视图是处理HTTP请求的功能，根据需要从数据库获取数据，通过使用HTML模板呈现此数据生成HTML页面，然后以HTTP响应返回HTML以显示给用户。索引视图遵循此模型 - 它提取有关数据库中有多少Book，BookInstance 可用 BookInstance 和 Author 记录的信息，并将其传递给模板以进行显示。

打开catalog/views.py，并注意该文件已经导入了 使用模板和数据生成HTML文件的 render() 快捷方式函数。

```
from django.shortcuts import render

# Create your views here.
```
复制以下代码。第一行导入我们将用于访问所有视图中数据的模型类
```
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )
```

视图函数的第一部分使用objects.all()模型类的属性来获取记录计数。它还会获取一个BookInstance状态字段值为“a”（可用）的对象列表。在函数结束时，我们将该函数称为render()创建和返回HTML页面作为响应。它将原始request对象，HTML模板以及context变量（Python字典）作为参数。

### Template（模板）

模版是定义一个文件（例如HTML页面）的结构与布局的文本文件，。Django将自动在应用程序“templates”目录查找模版。例如，在我们刚刚加的索引页，render() 函数会期望能够找到/locallibrary/catalog/templates/index.html这个文件，如何找不到该文件，则会引发错误。你可以看到访问 127.0.0.1:8000 现在将提供你一个相当直观的错误信息"TemplateDoesNotExist at /catalog/“以及其他详细信息

**扩展模版**

index模版将需要标准的HTML标记头部和正文，以及用于导航的部分（去我们尚为创建的网站其他的页面）以及一些介绍文本来展示我们图书数据。我们网站上的每一页，大部分文字（HTML和导航结构）都是一样的。Django模版语言不是强制开发人员在每个页面中复制这个“样板”，而是让你声明一个基本模版，然后再扩展它，仅替换每个特定页面不同的位置。

例如，基本模版 base_generic.html 可能看起来像下面的文本。正如你所见的，它包含一些“常见“HTML”和标题，侧边栏和使用命名 block 和 endblock 模版标记（粗体显示）标记的内容部分。块可以是空的，或者包含将被派生页“默认使用”的内容。

 模版标签（{% %}）,你可以在模版中使用函数循环列表，基于变量的值执行条件操作等。除了模版标签，模版语法允许你引用模版变量（通过从视图进入模版），并使用模版过滤器重新格式化变量（例如，将字符串设置为小写）。

```
<!DOCTYPE html>
<html lang="en">
<head>
  {% block title %}<title>Local Library</title>{% endblock %}
</head>

<body>
  {% block sidebar %}<!-- insert default navigation text for every page -->{% endblock %}
  {% block content %}<!-- default content text (typically empty) -->{% endblock %}
</body>
</html>
```
当我们要为特定视图定义一个模版时，我们首先指定基本模版（使用 extends 模版标签）。如果我们想要在模版中替换的部分，会使用 block/endblock 在基本模版表明。

例如，下面我们使用 extends 模版标签，并覆盖 content 块。生成的最终HTML将包含在基本模板中定义的所有HTML和结构（包括在标题栏中定义的默认内容），但插入新内容块代替默认内容块

```
{% extends "base_generic.html" %}

{% block content %}
<h1>Local Library Home</h1>
<p>Welcome to <em>LocalLibrary</em>, a very basic Django website developed as a tutorial example on the Mozilla Developer Network.</p>
{% endblock %}
```

**LocalLibrary基本模板**

下面就是我们的基本模版。正如所看到的，内容包括一些HTML和定义块 title ，sidebar 和 content。我们有默认的 title（当然我们可以改）和默认的所以图书和作者的链接列表 sidebar （我们可能并不会怎么改，但需要时，我们通过把想法放入块block中，比如想法是—允许范围）。创建一个新的文件 — locallibrary/catalog/templates/base_generic.html — 写入如下代码
```
<!DOCTYPE html>
<html lang="en">
<head>
  
  {% block title %}<title>Local Library</title>{% endblock %}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  
  <!-- Add additional CSS in static file -->
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>

<body>

  <div class="container-fluid">

    <div class="row">
      <div class="col-sm-2">
      {% block sidebar %}
      <ul class="sidebar-nav">
          <li><a href="{% url 'index' %}">Home</a></li>
          <li><a href="">All books</a></li>
          <li><a href="">All authors</a></li>
      </ul>
     {% endblock %}
      </div>
      <div class="col-sm-10 ">
      {% block content %}{% endblock %}
      </div>
    </div>

  </div>
</body>
</html>
```

该模版使用（并包含）JavaScript 和  Bootstrap  （css框架）来改进HTML页面的布局和显示，使用Bootstrap框架是创建一个可以在不同浏览器大小上很好地扩展的有吸引力的页面的快速方法，它还允许我们处理页面呈现而无需进入任何细节-我们只想关注服务器端代码.

基本模板还引用了一个本地css文件（styles.css），它提供了一些额外的样式。创建locallibrary/catalog/static/css/styles.css并为其提供以下内容：
```
.sidebar-nav {
    margin-top: 20px;
    padding: 0;
    list-style: none;
}
```

**index模版**
新建HTML文件 locallibrary/catalog/templates/index.html 写入下面代码。第一行我们扩展了我们的基本模版, 使用 content替换默认块。
```
{% extends "base_generic.html" %}

{% block content %}
<h1>Local Library Home</h1>

  <p>Welcome to <em>LocalLibrary</em>, a very basic Django website developed as a tutorial example on the Mozilla Developer Network.</p>

<h2>Dynamic content</h2>

  <p>The library has the following record counts:</p>
  <ul>
    <li><strong>Books:</strong> {{ num_books }}</li>
    <li><strong>Copies:</strong> {{ num_instances }}</li>
    <li><strong>Copies available:</strong> {{ num_instances_available }}</li>
    <li><strong>Authors:</strong> {{ num_authors }}</li>
  </ul>

{% endblock %}
```

在动态内容部分，我们已经为视图中包含的信息声明了占位符（模板变量）。变量使用“{{ }}”语法标记
注意区别模板变量和模板标签

这里需要注意的重要一点是，这些变量是用我们在视图的render()函数中传递给context的字典的key命名的渲染模板时，这些将被其关联值替换
```
return render(
    request,
    'index.html',
     context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
)
```
**在模版中引用静态文件**

你的项目可能会使用静态资源，包括javascript，css 和图像。由于这些文件的位置可能不知道（或者可能会发生变化），则Django允许你指定你的模版相对于这些文件的url, STATIC_URL （默认基本网站设置的值为“／static／”）。



在模版中，你首先调用 load 模板标签指定“ static”去添加此模版库。静态加载后，你可以使用 static 模版标签，指定文件相对URL
```
<!-- Add additional CSS in static file --> 
{% load static %} 
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```
你可以用同样的方式将图片添加到页面中：
```
{% load static %}
<img src="{% static 'catalog/images/local_library_model_uml.png' %}" alt="My image" style="width:555px;height:540px;"/>
```
在settings.py中添加以下代码，
```
STATIC_ROOT = BASE_DIR + '/catalog/static/'
```
STATIC_ROOT 全局指定静态文件位置