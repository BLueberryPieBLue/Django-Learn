####mysql的使用

> 免安装版本

- 解压mysql压缩包【记得解压的文件路径】

- 进行环境变量的配置

  - 我的电脑--》属性---》高级环境变量设置--》找到path --》新建--》将mysql的路径【bin的路径】直接复制粘贴

- 启动数据库

  - 先进入mysql的解压文件--》找到bin文件夹--》双击执行mysqld.exe文件

- 连接数据库

  - mysql -u root  -p
  - root【默认密码】

- 数据库连接成功之后，可以查看数据库

  - show  databases;  //查看数据库

  - use 数据库名  ;  //使用某个指定的数据库

  - show tables;  //查看所有的表

  - create database  数据库名;  //创建数据库

  - drop database 数据库名; //删除数据库

    

  - 