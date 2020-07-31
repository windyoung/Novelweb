[TOC]
# 个人笔记
## GIT
- git status 
- git add .
- git commit -m "备注"
- git pull 
- get push 
- ggit 脚本 自动三连提交 
## 技术方案
flask    
Vue3.0    
mysql   
- 前端vue3.0 优点  
    前后端分离  
    部署简单（哪怕你不懂怎么写代码也可以部署）
用处： 从后端读取数据， 展示页面
- 后端：flask  
    简单  
用处： 给前端提供API接口，从数据库读取数据  
***
## mysql
- #查看生成临时密码
- grep 'temporary password' /var/log/mysqld.log
### 登录
- mysql -u root -p # 回车输入你的新密码
- mysql -h localhost -u root -p books< ./books.sql  #从sqll恢复数据库
### 新建用户 bookbookwebweb
- #这个命令会让你创建一个能在本地登录的alex1943_read_books的帐号，密码为qwe123，并且允许远程登录
CREATE USER 'alex1943_read_books'@'%' IDENTIFIED BY 'qwe123';  
- #把这个数据库的所有权限赋予给这个alex1943_read_books这个账户  
GRANT ALL PRIVILEGES ON books.* TO 'alex1943_read_books'@'%';  
- #这条命令会让alex1943_read_books这个账户会有和root一样的权限  
GRANT ALL PRIVILEGES ON *.* TO 'alex1943_read_books'@'%';  
**这条是正确的打开方式 ** 
GRANT select ON books.* TO 'alex1943_read_books'@'%';  
- #刷新权限
FLUSH PRIVILEGES;  
### 修改密码 
- ALTER USER USER() IDENTIFIED BY '你自己设置的密码';
### 禁止  mysql root 远程登录
- update user set host = "localhost" where user = "root" and host = "%";
- FLUSH PRIVILEGES;
***
## CENTOS7 
### 防火墙
- iptables -I INPUT -p tcp --dport 23306 -j ACCEPT
### 磁盘挂载
- 挂载磁盘 mount /dev/mapper/data_ssd_0-database  /database_data 
- 设置开机自动挂载需要修改/etc/fstab文件
在文件的最后增加一行  /dev/mapper/data_ssd_0-database  /database_data  defaults 1 2
***
## python
### virtualenv
cd /home/vscweb/project_code/Novelweb/books_flask  
创建virtualenv -p python3 .book_flask_env   
使用 source .book_flask_env/bin/activate  
退出 deactivate


********
********
# 问题处理
## CENTOS7 问题合集
#### 磁盘挂载后进入应急模式 
进入系统输入 root 密码 ,  取消对 /etc/fstab文件 的修改   
查询 磁盘的UUID : lsblk -f    
**解决方案** 挂载时使用 UUID 挂载 ::UUID=5d36d146-649c-4a39-8d69-33f91ea4f561  /database_data ext4    defaults        0 0  


***
## mysql 安装 问题集合
### ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/database_data/mysql/mysql_mysql.sock' (2) 
- 产生此问题的原因一般有两个：   
1、mysql服务未正常运行：由于mysql的socket文件是由mysqld服务启动时创建的，如果mysqld服务未正常启动，socket文件自然也不会被创建，当然会找不到socket文件了。对于判断mysql服务是否启动，我们可以使用下面命令：    
1.1、 端口是否打开 lsof -i:3306     
1.2、mysqld服务是否正在运行  service mysqld status    
2、socket文件路径在配置文件中设置不完整：   
这一般是由于我们修改了mysql配置“/etc/my.cnf”引起的。   
比如我们修改了配置文件中“[mysql]”选项下的“socket”参数，而未指定“[client]”、“[mysql]”选项的“socket”参数，导致mysql使用默认的socket文件位置去寻找socket文件，从而导致未找到socket文件而引发此错误。   
如果确认mysql服务正常运行，还提示文章标题的此错误，那就是“/etc/my.cnf”配置文件的问题了。     
- **解决办法**是修改“/etc/my.cnf”配置文件，在配置文件中添加“[client]”选项和“[mysql]”选项，并使用这两个选项下的“socket”参数值，与“[mysqld]”选项下的“socket”参数值，指向的socket文件路径完全一致。    
[mysqld]   
datadir=/storage/db/mysql   
socket=/storage/db/mysql/mysql.sock   
[client]   
default-character-set=utf8   
socket=/storage/db/mysql/mysql.sock   
[mysql]   
default-character-set=utf8   
socket=/storage/db/mysql/mysql.sock   
其中socket等于的路径就是socket文件的位置，我们只要修改my.cnf文件,告诉mysql，mysqldump，mysqladmin等命令，mysql服务的socket文件位置在哪里，然后重启mysqld服务即可。  
### [ERROR] InnoDB: Operating system error number 13 in a file operation.
**system error number 13**: 权限问题  
**解决方案**关闭 selinux ：setenforce 0 
不关闭 selinux ?????? chown -R mysql:mysql ./mysql/ ?????? 重启时测试下 