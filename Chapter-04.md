# 第四天
##  Django介绍
Django是一个高级Python Web框架，鼓励快速开发和实用的设计。
由经验丰富的开发人员开发，它可以处理Web开发的大部分问题，
因此可以专注于编写应用程序，而无需重新发明轮子。

Django 特点
1.  快速: Django旨在帮助开发人员尽可能快地完成应用程序
2.  安全: Django严肃对待安全并帮助开发人员避免许多常见的安全错误
3.  可伸缩:  Django快速灵活扩展的能力
4.  丰富的组件: Django 内置各种web开发常用功能组件

## Django安装
使用pycharm安装Django
File=>Setting=>Project:项目名=>Project Interpreter=>点击右侧+号= >在搜索框输入django=> 在列表中选中django=>点击install

使用pip
````
pip install django
````

验证django
````
>>> import django
>>> django.get_version()
'2.0.5'

````

## 创建一个项目

在pycharm Terminal中输入
````
django-admin startproject mysite
````

项目结构
````
└── mysite
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

````
+ 顶部mysite:  项目根目录。 它的名字与Django无关; 你可以将它重命名为任何你喜欢的名字
+ manager.py: 一个命令行实用程序，可让您以各种方式与此Django项目进行交互。
+ 内部mysite: 项目的实际Python包。 它的名字是你需要用来导入任何东西的Python包名
+ mysite/__init__.py: 一个空文件，告诉Python这个目录应该被视为一个Python包
+ mysite/settings.py:  这个Django项目的配置文件
+ mysite/urls.py:  这个Django项目的URL声明
+ mysite/wsgi.py:  WSGI兼容的Web服务器,为项目提供服务的入口点

以开发模式运行服务器

````
cd mysite
python manage.py runserver
````

访问django项目
在浏览器打开http://127.0.0.1:8000

修改开发服务器默认端口
````
d mysite
ython manage.py runserver 8080
````

默认开发服务器监听127.0.0.1
修改监听ip
````
python manage.py runserver 0:8000
````

## 创建第一个app
项目和应用程序有什么区别？ 应用程序是一种Web应用程序，它可以执行某些操作，
例如博客系统，公共记录数据库或简单的民意调查应用程序。 
项目是特定网站的配置和应用程序的集合。 项目可以包含多个应用程序。

````
python manage.py startapp myapp
````

myapp目录结构

````
myapp
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
````

admin.py  将models注册到djangoadmin
apps.py  app 配置
__init__.py  表明该文件夹为包
migrations  数据库版本升级
models.py 数据库管理
tests.py  测试文件
views  视图文件

编辑myapp/views.py
````

````

创建myapp/urls.py

````
from django.urls import path

from .  import views


urlpatterns = [
    path('', views.index, name='index')
]

````

编辑mysite/urls.py

````
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls'))
]
````

path 函数定义了4个参数， 两个必须的，route和view，两个可选的name和kwargs

path()参数 route

路由是一个包含URL模式的字符串。处理请求时，Django从urlpatterns中的第一个模式开始，
并在列表中向下，并将请求的URL与每个模式进行比较，直到找到匹配的模式。
不搜索GET和POST参数或域名。
例如，在https://www.example.com/myapp/的请求中，URLconf将查找myapp/。
 在https://www.example.com/myapp/?page=3的请求中，URLconf也会查找myapp/。
 
 path() 参数view
 当Django找到匹配的模式时，它将HttpRequest对象作为第一个参数，并
 将路由中的任何“捕获”值作为关键字参数调用指定的视图函数。
 
 patch() 参数name
 
 命名URL可以让你从Django其他地方明确地引用它，特别是在模板中


