#  第九天

开始一个新项目
+ 使用django的工具创建一个网站项目和应用
+ 创建模型（models）
+ 使用django的admin站点来填充网站数据
+ 创建视图函数（views）来取回相应的数据，并用模板（templates）渲染成HTML页面
+ 创建urlconf，将不同的url分发给特定的视图函数（views）
+ 添加用户认证和会话（sessions）
+ 表单
+ 编写单元测试

## 创建一个新的项目
创建一个图书管理项目，这个网站的目标是为一个小型的图书馆提供一个在线的目录。在这个小型图书管里，用户能浏览书籍和管理他们的账户。

### 搭建网站框架
1. 使用django-admin 工具创建项目文件夹
2. 使用manager.py创建一个应用
3. 在项目配置文件（settings.py）中注册应用
4. 为应用分配url

### 创建项目
```
django-admin startproject locallibrary
cd locallibrary
```
django-admin 工具创建如下所示的目录结构
```
locallibrary/
├── locallibrary
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

```
locallibrary文件夹是整个网站的进入点
+ settings.py 包含所有的网站设置。这是可以注册所有创建的应用的地方，也是静态文件，数据库配置的地方，等等
+ urls.py 定义了网站url到view的映射。虽然这里可以包含所有的url，但是更常见的做法是把应用相关的url包含在相关应用中
+ wsgi.py 帮助Django应用和web服务器间的通讯
+ manage.py 可以创建应用，操作数据库，启动开发服务器

### 创建catalog应用
接下来，在locallibrary项目里，使用下面的命令创建catalog应用
```
python manage.py startapp catalog
```
这个工具创建了一个新的文件夹，并为该应用创建了不同的文件
```
locallibrary/
├── catalog
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── locallibrary
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
+ views.py 视图
+ models.py 模式
+ tests.py 测试
+ admin.py 网站管理
+ apps.py  注册应用
+ migration文件夹，用来存储“migrations”——当你修改你的数据模型时，这个文件会自动升级你的数据库。
+ __init__.py — 一个空文件，声明模块

注意：这时文件夹locallibrary下面有urls.py,应用catalog下没有urls.py,我们后面添加

### 注册catalog应用

既然应用已经创建好了，我们还必须在项目里注册它，以便工具在运行时它会包括在里面（比如在数据库里添加模型时）。在项目的settings里，把应用添加进INSTALLED_APPS ，就完成了注册。

打开项目设置文件 locallibrary/locallibrary/settings.py 找到  INSTALLED_APPS 列表里的定义。 如下所示，在列表的最后添加新的一行catalog.apps.CatalogConfig

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog.apps.CatalogConfig', 
]
```

新的这行详细说明了应用配置文件在 (CatalogConfig) /locallibrary/catalog/apps.py 里，当你创建应用时就完成了这个过程。

注意：注意到INSTALLED_APPS已经有许多其他的应用了 (还有 MIDDLEWARE, 在settings的下面)。这些应用为  Django administration site 提供了支持和许多功能(包括会话，认证系统等)。

### 配置数据库
sqllite
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
mysql
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'locallibrary',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

注意：mysql需要安装mysqlconnect模块，并现在mysql数据库中创建出一个数据库

### 其他配置

settings.py里还包括其他的一些设置，现在只需要改变时区。
```
TIME_ZONE = 'Asia/Shanghai'
```

### 配置urlconf

打开locallibrary/locallibrary/urls.py 注意指导文字解释了一些使用URL映射器的方法。
```
"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

```

URL 映射通过urlpatterns 变量管理，它是一个path() 函数的Python列表。 每个path()函数要么将URL式样(URL pattern)关联到特定视图(specific view)，当模式匹配时将会显示，要么关联到某个URL式样列表函数。urlpatterns 列表最开始定义了把所有URL映射到admin.site.urls这个函数。这个函数包含了Administration 应用自己的URL映射定义。

在urlpatterns 列表的下面一行插入下面的代码。这个新的URL定义把所有的catalog式样的网络请求放在模块 catalog.urls里处理 (使用相对路径 URL /catalog/urls.py).
```
from django.conf.urls import include, url

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
```

现在我们把我们网站的根URL(例如127.0.0.1:8000)URL 127.0.0.1:8000/catalog/; 这是项目中唯一的应用，所以我们最好这样做。为了完成这个目标，我们使用一个特别的视图函数(RedirectView), 当url函数中的url式样被识别以后（在这个例子中是根url），就会把RedirectView里的第一个相对路径参数重定向到（/catalog）。

```
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/')),
]
```

Django 默认不会提供CSS, JavaScript, 和图片等静态文件 。但是当你在开发环境中开发时，这些静态文件也很有用。在URL配置李，你可以加上下面的代码在开发环境中使用静态文件。
```
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

注意： 我们也可以用下面的方法
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

在catalog文件夹里创建一个名为 urls.py 的文件, 添加下面的代码urlpatterns. 我们会在编写应用时添加相关式样。
```
from django.urls import path

from . import views


urlpatterns = [

]
```

### 测试网站框架

Django 使用对象关系映射器（ORM）将Django代码中的模型定义映射到底层数据库使用的数据结构。当我们更改模型定义时，Django会跟踪更改并创建数据库迁移脚本 (in /locallibrary/catalog/migrations/) 来自动迁移数据库中的底层数据结构

当我们创建网站时，Django会自动添加一些模型供网站的管理部分使用（稍后我们会解释）。运行以下命令来定义数据库中这些模型的表（确保你位于包含 manage.py 的目录中):

```
python manage.py makemigrations
python manage.py migrate
```
注意： 每次模型改变，都需要运行以上命令，来影响需要存储的数据结构（包括添加和删除整个模型和单个字段）

makemigrations 命令创建（但不适用）项目中安装的所有应用程序的迁移（你可以指定应用程序名称，也可以为单个项目运行迁移）
这 migrate 命令 明确应用迁移你的数据库（Django跟踪哪些已添加到当前数据库）

### 运行网站
```
python manage.py runserver
```

## 使用模型