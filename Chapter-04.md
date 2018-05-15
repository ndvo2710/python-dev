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