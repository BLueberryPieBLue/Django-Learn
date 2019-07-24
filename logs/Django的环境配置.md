#### Django的环境配置

- python环境是ok的

- pip是可用的

  - pip用来安装第三方包的

- 创建虚拟环境【可以先不写】

  - linux/mac
  - windows

- 安装Django

  ```python
  pip install django==1.11.7
  ```

- django安装成功之后，创建项目

  创建项目之前首先新建一个目录【文件夹】

  进入这个目录之后执行

  ```python
  django-admin  startproject  projectname
  #django-admin  startproject  项目名
  ```

- 使用pycharm打开项目的时候，要在manage.py的上一级打开

  - manage所在的文件夹

- 当进入pychram之后，我们可以使用自带终端来创建app

```
python manage.py  startapp  appname
```

- 当app创建完成之后，需要在setting.py文件中配置

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "App",#添加我们创建的app
]
```

- 在setting.py文件中

- ```python
  ALLOWED_HOSTS = ["*"]
  #允许所有人访问
  ```

- 在setting.py文件中

  ```python
  #设置语言
  LANGUAGE_CODE = 'zh-hans'
  #设置时区
  TIME_ZONE = 'Asia/Shanghai'
  ```

- 运行当前项目

```python
python manage.py  runserver  
```

- 运行成功，在浏览器访问

```
 http://127.0.0.1:8000/
 #会显示正常工作
```

- 添加一个路由，在urls.py文件中添加

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # alt+enter  添加,需要导包，App下面的views
    url(r"^login/",views.login),
]
```

- 需要在app中的views.py去创建视图函数login

  ```python
  def login(request):
      #必须返回的是httpResponse对象
      return HttpResponse("你真是一个小机灵鬼！！！")
  ```

- 执行python manage.py  runserver 将服务器重新部署

- 在浏览器访问的时候，这时候需要使用

  ```
   http://127.0.0.1:8000/login
  ```

  