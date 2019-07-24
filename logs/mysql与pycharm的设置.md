#### mysql与pycharm的设置

- 保证mysql已经安装成功

- 使用终端在mysql中创建一个数据库

- ```python
  mysql -u root -p
  ***
  #连接数据库
  mysql> show databases;
  #查看当前数据库
  mysql> create database tour;
  #创建数据库  tour：数据库名，可以自己命名
  ```

- 找到setting.py文件，并在添加如下代码

```python

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tour', #数据库名字
        "USER":"root",  #数据库用户名
        "PASSWORD":"root", #数据库的密码
        "HOST":"127.0.0.1", #ip地址
        "PORT":"3306",# 端口号
    }
}
```

**注意**：在使用数据库的时候，必须保证数据库的服务是开启的状态

> net start mysql

找到mysql的安装地址，找到bin文件夹，到bin文件夹下面找到mysqld.exe，双击执行

- 到与setting.py同目录的__init__.py文件下，添加以下代码

- ```python
  import pymysql
  
  pymysql.install_as_MySQLdb()
  ```

**注意**若没有安装pymysql模块，则会报错，需要将pymsql模块安装

```python
1.使用pycharm安装
2.使用pip安装
pip install pymsql
```

- 当项目创建之后，配置完成之后，我们执行一下迁移【因为只有执行迁移的时候，才会在数据库中生成表】

- ```python
  python manage.py migrate
  ```

- 需要在models.py文件中创建一个类，并且这个类必须要继承models.Model

- ```python
  class User(models.Model):
      username = models.CharField(max_length=20)
      password = models.CharField(max_length=20)
      #CharField 指定字段的类型
      #max_length 指定字段的最大长度
  ```

  - 生成迁移文件

  - ```pyhthon
    python manage.py makemigrations
    ```

  - 执行迁移文件

  - ```python
    python manage.py  migrate
    ```

    

  
  

  

  

