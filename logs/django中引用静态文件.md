#### django中引用静态文件

> 当我们将我们的html文件放到Templates文件中的时候，这时候此html我们可以直接引用，
>
> 若出现这个html文件，它还引用了其他的一些文件【js，css，img】，这是就需要引用django中静态的文件

- 需要在Templates的同级目录下创建一个static目录
- 需要在setting文件中添加代码

```python
#默认自带的
STATIC_URL = '/static/'
#添加代码
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```

- 将html需要用到的资源，放在static目录下

- 在html中引用静态资源

- ```html
  <head>
  		<meta charset="UTF-8">
  		<title></title>
          <script src="/static/js/jquery-2.1.0.js" type="text/javascript" charset="utf-8"></script>
  
  		<link rel="stylesheet" type="text/css" href="/static/css/style.css"/>
  	</head>
  ```

- 配置路由，在urls.py文件中配置

- ```python
  urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r"^getlogin",views.getlogin)
  ]
  ```

- 需要在views.py文件中创建getlogin函数

- ```python
  
  def getlogin(request):
      #返回登录的页面
      return render(request,"login.html")
  ```

- 启动服务

- ```
  python manage.py runserver  127.0.0.1:9000
  ```

  

- 如何请求接口

- ```
   http://127.0.0.1:9000/getlogin
  ```

  

- 