# 第十一天

## django session

我们在之前的教程中创建的LocalLibrary网站，允许用户浏览目录中的书本和作者。虽然内容是从数据库动态生成的，但每个用户在使用站点时，基本上都可以访问相同的页面，和相同类型的信息。

在一个 “真实” 的图书馆中，您可能希望根据用户之前对站点的使用，首选项等，为个人用户提供自定义体验。例如，您可以在用户下次访问时，隐藏上次已经确认的警告消息。网站，或存储和尊重他们的偏好（例如，他们希望在每个页面上显示的搜索结果的数量）。

session允许实现此类行为，允许基于每个站点访问者，显示不同的内容

### 什么是session

Web浏览器和服务器之间的所有通信，都是通过HTTP协议进行的，该协议是无状态的。协议无状态的事实，意味着客户端和服务器之间的消息，完全相互独立 - 没有基于先前消息的“序列”或行为的概念。因此，如果想拥有一个追踪与客户的持续关系的网站，需要自己实现。

session用于跟踪站点和特定浏览器之间“状态”的机制。会话允许您为每个浏览器存储任意数据，并在浏览器连接时，将该数据提供给站点。然后，通过“kye”引用与会话相关联的各个数据项，“key”用于存储和检索数据。

Django使用包含特殊session ID的cookie，来识别每个浏览器，及其与该站点的关联会话。默认情况下，实际会话数据存储在站点数据库中，您可以将Django配置为，将会话数据存储在其他位置（缓存，文件）

### 启用session

django项目默认会启用session

配置在项目文件（locallibrary/locallibrary/settings.py）的INSTALLED_APPS 和 MIDDLEWARE 部分中设置，如下所示

```
INSTALLED_APPS = [
    ...
    'django.contrib.sessions',
    ....

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    ....
```

### 使用session
你可以从request请求参数访问视图中的session会话属性（作为视图的第一个参数传入的HttpRequest）。此会话属性，表示与当前用户的特定连接（或者更确切地说，是与当前浏览器的连接，由此站点的浏览器cookie中的会话ID标识）。

会话session属性是一个类似字典的对象，您可以在视图中多次读取和写入，并根据需要进行修改。您可以执行所有常规的字典操作，包括清除所有数据，测试是否存在密钥，循环数据等。大多数情况下，您只需使用标准 “字典” API，来获取和设置值。

下面的代码片段，显示了如何使用与当前会话（浏览器）关联的密钥“my_car”来获取，设置和删除某些数据。

```
# Get a session value by its key (e.g. 'my_car'), raising a KeyError if the key is not present
my_car = request.session['my_car']

# Get a session value, setting a default if it is not present ('mini')
my_car = request.session.get('my_car', 'mini')

# Set a session value
request.session['my_car'] = 'mini'

# Delete a session value 
del request.session['my_car']
```
API还提供了许多其他方法，主要用于管理关联的会话cookie。例如，有一些方法，可以测试客户端浏览器，是否支持cookie，设置和检查cookie过期日期，以及从数据存储中清除过期的会话。你可以在[如何使用会话](https://docs.djangoproject.com/en/2.0/topics/http/sessions/)中找到完整的API。


### 简单的例子 - 获取访问次数

作为一个简单的现实世界的例子，我们将更新我们的图书馆，告诉当前用户，他们访问 LocalLibrary 主页的次数。

打开/locallibrary/catalog/views.py，做以下更改
```
# Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    
    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context=context)
```

这里，我们首先得到 session key  'num_visits'的值，如果之前没有设置，则将值设置为0。每次收到请求时，我们都会递增该值，并将其存回会话中（下次用户访问该页面时）。然后将num_visits变量，传递给上下文变量中的模板。


编辑locallibrary/catalog/templates/index.html
```
<h2>Dynamic content</h2>

<p>The library has the following record counts:</p>
<ul>
  <li><strong>Books:</strong> {{ num_books }}</li>
  <li><strong>Copies:</strong> {{ num_instances }}</li>
  <li><strong>Copies available:</strong> {{ num_instances_available }}</li>
  <li><strong>Authors:</strong> {{ num_authors }}</li>
</ul>

<p>You have visited this page {{ num_visits }}{% if num_visits == 1 %} time{% else %} times{% endif %}.</p>
```

## 身份验证和授权

Django 提供了一个身份验证和授权（“权限”）系统，该系统构建在的session框架之上，允许你验证用户凭据，并定义每个用户可允许执行的操作。该框架包括用户Users和分组Groups的内置model（一次向多个用户应用权限的通用方法），用于登录用户的权限/标志，以指定用户是否可以执行任务，表单和视图，以及查看限制内容的工具。


下面演示如何在LocalLibrary网站中，启用用户身份验证，创建自己的登录和注销页面，为模型添加权限，以及控制对页面的访问。我们将使用身份验证/权限，来显示用户和图书馆员借用图书的列表。

### 启用身份验证

django 默认启用身份验证功能

配置在项目文件（locallibrary/locallibrary/settings.py）的INSTALLED_APPS和MIDDLEWARE部分中设置，如下所示

```
INSTALLED_APPS = [
    ...
    'django.contrib.auth',  #Core authentication framework and its default models.
    'django.contrib.contenttypes',  #Django content type system (allows permissions to be associated with models).
    ....

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',  #Manages sessions across requests
    ...
    'django.contrib.auth.middleware.AuthenticationMiddleware',  #Associates users with requests using sessions.
    ....
```

### 创建用户和分组

我们已经创建了第一个用户（这是一个超级用户，使用命令 python manage.py createsuperuser 创建）。我们的超级用户已经过身份验证，并拥有所有权限，因此我们需要创建一个测试用户，来代表普通网站用户。我们将使用管理站点，来创建我们的 locallibrary 组別和网站登录，因为这是最快的方法之一。


### 设置身份验证视图

Django 提供了创建身份验证页面所需的几乎所有功能，让处理登录，注销和密码管理等工作，都能 “开箱即用”。这些相关功能包括了 url 映射器，视图和表单，但它不包括模板 - 我们必须创建自己的模板！

在本节中，我们将展示如何将默认系统，集成到 LocalLibrary 网站并创建模板。我们将它们放在主项目的 URL 当中。


将以下内容，添加到项目 urls.py（locallibrary/locallibrary/urls.py）文件的底部
```
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
```

添加后打开http://127.0.0.1:8000/accounts/ 会显示404 


我们访问http://127.0.0.1:8000/accounts/login/ 会显示找不到模板registration/login.html

###  模板目录

我们希望在模板搜索路径中的目录 /registration/ 某处，找到刚刚添加的 url（以及隐式视图）的关联模板。

对于此站点，我们将 HTML 页面，放在 templates/registration/ 目录中。此目录应该位于项目的根目录中，即与 catalog 和 locallibrary 文件夹相同的目录）。请立即创建这些文件夹。 
```
locallibrary (django project folder)
   |_catalog
   |_locallibrary
   |_templates (new)
                |_registration
```

注意改templates文件夹要和manage.py在同一目录
修改settings.py

 ```
 TEMPLATES = [
    {
        ...
        'DIRS': ['./templates',],
        'APP_DIRS': True,
        ...
 ```

### 登录模板
创建一个名为 locallibrary/templates/registration/login.html 的新HTML文件。为它加入以下内容：
```
{% extends "base_generic.html" %}

{% block content %}

{% if form.errors %}
  <p>Your username and password didn't match. Please try again.</p>
{% endif %}

{% if next %}
  {% if user.is_authenticated %}
    <p>Your account doesn't have access to this page. To proceed,
    please login with an account that has access.</p>
  {% else %}
    <p>Please login to see this page.</p>
  {% endif %}
{% endif %}

<form method="post" action="{% url 'login' %}">
{% csrf_token %}

<div>
  <td>{{ form.username.label_tag }}</td>
  <td>{{ form.username }}</td>
</div>
<div>
  <td>{{ form.password.label_tag }}</td>
  <td>{{ form.password }}</td>
</div>

<div>
  <input type="submit" value="login" />
  <input type="hidden" name="next" value="{{ next }}" />
</div>
</form>

{# Assumes you setup the password_reset view in your URLconf #}
<p><a href="{% url 'password_reset' %}">Lost password?</a></p>

{% endblock %}
 ```
如果尝试登录，登录后默认将跳转到http://127.0.0.1:8000/accounts/profile/ 但我们没有定义该url将导致404错误，修改默认跳转url

打开项目设置（locallibrary/locallibrary/settings.py），并将下面的文本添加到底部。现在登录时，应该默认重定向到站点主页。

```
# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
```

### 登出模板

如果打开登出网址（http://127.0.0.1:8000/accounts/logout/），那么会看到一些奇怪的行为 - 所属的用户肯定会被登出，但您将被带到管理员登出页面。这不是想要的，只是因为该页面上的登录链接，带到管理员登录屏幕（并且仅对具有is_staff权限的用户可用）。

创建并打开 locallibrary/templates/registration/logged_out.html。将下面的文字，复制到文档中：
```````
{% extends "base_generic.html" %}

{% block content %}
<p>Logged out!</p>  

<a href="{% url 'login'%}">Click here to login again.</a>
{% endblock %}
```

### 密码重置
http://127.0.0.1:8000/accounts/password_change/
创建模板 locallibrary/templates/registration/password_change_form.html

```
{% extends "base_generic.html" %}
{% load i18n static %}


{% block content %}<div id="content-main">

<form method="post">{% csrf_token %}
<div>
{% if form.errors %}
    <p>
    {% if form.errors.items|length == 1 %}{% trans "Please correct the error below." %}{% else %}{% trans "Please correct the errors below." %}{% endif %}
    </p>
{% endif %}


<p>{% trans "Please enter your old password, for security's sake, and then enter your new password twice so we can verify you typed it in correctly." %}</p>



<div >
    {{ form.old_password.errors }}
    {{ form.old_password.label_tag }} {{ form.old_password }}
</div>

<div>
    {{ form.new_password1.errors }}
    {{ form.new_password1.label_tag }} {{ form.new_password1 }}
    {% if form.new_password1.help_text %}
    <div class="help">{{ form.new_password1.help_text|safe }}</div>
    {% endif %}
</div>

<div>
{{ form.new_password2.errors }}
    {{ form.new_password2.label_tag }} {{ form.new_password2 }}
    {% if form.new_password2.help_text %}
    <div class="help">{{ form.new_password2.help_text|safe }}</div>
    {% endif %}
</div>


<div>
    <input type="submit" value="{% trans 'Change my password' %}"/>
</div>

</div>
</form></div>

{% endblock %}

```

创建模板locallibrary/templates/registration/password_change_done.html
```
{% extends "base_generic.html" %}

{% load i18n %}
{% block content %}

<p>{% trans 'Your password was changed.' %}</p>
{% endblock %}
```

## 验证已登录的用户

本节介绍如何根据用户是否登录，来有选择地控制用户看到的内容

### 模板

可以使用`{{ user }}`模板变量，以获取有关模板中，当前登录用户的信息（默认情况下，在我们在骨架中设置项目时，会将其添加到模板上下文中）。

通常，您将首先针对`{ user.is_authenticated }}`板变量进行测试，以确定用户是否有资格查看特定内容。为了证明这一点，接下来我们将更新侧边栏以在用户未登录时显示“登录”链接，如果他们已登录则显示“退出”链接。

打开基本模板（/locallibrary/catalog/templates/base_generic.html）并将以下文本复制到侧边栏块中，紧接在endblock模板标记之前

```
<ul class="sidebar-nav">

    ...

   {% if user.is_authenticated %}
     <li>User: {{ user.get_username }}</li>
     <li><a href="{% url 'logout'%}?next={{request.path}}">Logout</a></li>   
   {% else %}
     <li><a href="{% url 'login'%}?next={{request.path}}">Login</a></li>   
   {% endif %} 
  </ul>
```
打开页面查看http://127.0.0.1:8000/catalog/

我们使用if-else-endif模板标签根据`{{ user.is_authenticated }}`是否为true来有条件地显示文本。如果用户已通过身份验证，那么我们知道我们拥有有效用户，因此我们会调用`{{ user.get_username }}`来显示其名称。

我们使用url模板标记和相应URL配置的名称创建登录和退出URL。另请注意我们如何将“next = \ {{ request.path }}附加到URL的末尾。这样做是将包含当前页面地址（URL）的URL参数添加到链接URL的末尾。用户成功登录/注销后，视图将使用此“next”将用户重定向回他们首次单击登录/注销链接的页面

### 视图

如果你正在使用基于函数的视图，则限制对函数的访问的最简单方法是将login_required装饰器应用于您的视图函数，如下所示。如果用户已登录，则您的视图代码将正常执行。

```
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
```
在基于类的视图中限制对登录用户的访问的最简单方法是从LoginRequiredMixin派生。需要在主视图类之前的超类列表中首先声明此mixin。

```
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    ...
```
我们将现有的视图加上登录验证
## 列出当前用户借阅的书
让我创建一个页面展示用户借阅的书
### 模板

首先，我们必须让用户可以租借BookInstance（我们已经拥有状态和due_back日期，但我们在这个模型和用户之间没有任何关联。我们将创建一个使用ForeignKey（一对多）字段。我们还需要一个简单的机制来测试借出的书是否过期。

打开catalog/models.py，然后从django.contrib.auth.models导入User模型（在文件顶部的上一个导入行的正下方添加它，因此用户可以使用后续代码）：

```
from django.contrib.auth.models import User
```

接下来将借用者字段borrower，添加到BookInstance模型：

```
borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
```

当我们在这里时，让我们添加一个属性，我们可以从模板中调用它来判断特定的书籍实例是否过期。添加在BookInstance 底部
```
from datetime import date  #这行放到文件头部

@property
def is_overdue(self):
    if self.due_back and date.today() > self.due_back:
        return True
    return False
```

现在我们已经更新了模型，我们需要对项目进行新的迁移，然后应用这些迁移：
```
python manage.py makemigrations
python manage.py migrate
```

### djangoadmin

现在打开 catalog/admin.py，并将borrower字段，添加到BookInstanceAdmin类别中的list_display和fieldsets，如下所示。这将使该字段在Admin部分中可见，以便我们可以在需要时将User分配给BookInstance。

```
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
```

### 借书

现在可以将书本借给特定用户，然后借出一些BookInstance记录。将他们的借用字段borrowed，设置为您的测试用户，将状态status设置为 “On loan”，并在设置截止日期。

### 已借书视图

现在我们将添加一个视图，以获取已经借给当前用户的所有书本列表。我们将使用我们熟悉的、基于类的通用类列表视图，但这次我们还将导入并派生自LoginRequiredMixin，以便只有登录用户才能调用此视图。我们还将选择声明template_name，而不是使用默认值
将以下内容添加到 catalog/views.py：

```
class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
```

为了将查询，限制为当前用户的BookInstance对象，我们重新实现了get_queryset()，如上所示。请注意，“o”是表示借出当中“on loan”的存储代码，我们按due_back日期排序.

### url 
catalog/urls.py

```
path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
```

### 模板

现在，我们需要为此页面添加一个模板。首先，创建模板文件catalog/templates/catalog/bookinstance_list_borrowed_user.html，并为其提供以下内容
```
{% extends "base_generic.html" %}

{% block content %}
    <h1>Borrowed books</h1>

    {% if bookinstance_list %}
    <ul>

      {% for bookinst in bookinstance_list %} 
      <li class="{% if bookinst.is_overdue %}text-danger{% endif %}">
        <a href="{% url 'book-detail' bookinst.book.pk %}">{{bookinst.book.title}}</a> ({{ bookinst.due_back }})        
      </li>
      {% endfor %}
    </ul>

    {% else %}
      <p>There are no books borrowed.</p>
    {% endif %}       
{% endblock %}
```
### 更新侧栏

最后一步，是将这个新页面的链接，添加到侧边栏中。我们将把它放在我们为登录用户显示其他信息的同一部分。
打开基本模板（locallibrary/catalog/templates/base_generic.html），如下所示。
```
<ul class="sidebar-nav">
   {% if user.is_authenticated %}
   <li>User: {{ user.get_username }}</li>
   <li><a href="{% url 'my-borrowed' %}">My Borrowed</a></li>
   <li><a href="{% url 'logout'%}?next={{request.path}}">Logout</a></li>   
   {% else %}
   <li><a href="{% url 'login'%}?next={{request.path}}">Login</a></li>   
   {% endif %} 
 </ul>
```

## 权限

在本文前面，我们向您展示了，如何为当前用户创建一个页面，列出他们借用的书本。现在的挑战，是创建一个只对图书馆员可见的类似页面，它显示所有借用的书本，其中包括每个借用人的名字。
判断是否管理员：
模板使用 user.is_staff
视图使用 @staff_member_required
url catalog/borrowed


### 视图

现在我们将添加一个视图，以获取已经借出所有书本列表。我们将使用我们熟悉的、基于类的通用类列表视图，但这次我们还将导入PermissionRequiredMixin，以便只有管理员才能调用此视图。我们还将选择声明template_name，而不是使用默认值
将以下内容添加到 catalog/views.py：

```
class BorrowedAllBookListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_admin.html'
    permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')
```

使用permission_required字段指定需要的权限

### url
```
path('borrowed/', views.BorrowedAllBookListView.as_view(), name='admin-borrowed'),
```

### 模板
现在，我们需要为此页面添加一个模板。首先，创建模板文件catalog/templates/catalog/bookinstance_list_borrowed_admin.html，并为其提供以下内容

```
{% extends "base_generic.html" %}

{% block content %}
    <h1>Borrowed books</h1>

    {% if bookinstance_list %}
    <ul>

      {% for bookinst in bookinstance_list %} 
      <li class="{% if bookinst.is_overdue %}text-danger{% endif %}">
        <a href="{% url 'book-detail' bookinst.book.pk %}">{{bookinst.book.title}}</a> ({{ bookinst.due_back }}) borrower {{ bookinst.borrower}}    
      </li>
      {% endfor %}
    </ul>

    {% else %}
      <p>There are no books borrowed.</p>
    {% endif %}       
{% endblock %}
```

###  更新侧栏
打开基本模板（locallibrary/catalog/templates/base_generic.html），如下所示。

```
          <li><a href="{% url 'my-borrowed' %}">My Borrowed</a></li>
          {% if perms.catalog.can_mark_returned %}
          <li><a href="{% url 'admin-borrowed' %}">admin Borrowed</a></li>
          {% endif %}
```

