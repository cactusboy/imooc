#### 20180909
### mac下安装mysqlclient模块的注意事项
由于需要在mac下配置python3的开发环境,需要安装flask和mysqlclient,在虚拟环境下安装mysqlclient出错,
于是记录下踩坑过程:
1:在mac下的python3.7的虚拟环境中安装mysqlclient时出错:
" OSError: mysql_config not found"
原因是没有安装mysql的配置模块"mysql-connector-c"
打开一个终端窗口,安装mysql-sonnector-c
``` 
$ brew install mysql-connector-c
```
安装完成后,运行pip install mysqlclient还是会出错,因为mysql_config文件还没有配置(出于官方的原因,需要手动修改mysql_config文件才能正确安装)
2,修改mysql_config文件
进入配置文件所在目录
``` 
$ cd /usr/local/cellar/mysql-connector-c/6.1.11/bin
```
其中:6.1.11是版本目录,根据自己安装的版本会有变动.
使用vim编辑mysql_config文件,在第112行附近代码如下:
```
# Create options
libs="-L$pkglibdir"
libs="$libs -l "
embedded_libs="-L$pkglibdir"
embedded_libs="$embedded_libs -l "
```
将(libs="$libs -l -lssl -lcrypto ")改成
(libs="$libs -lmysqlclient -lssl -lcrypto ")
如下图:
```
# Create options
libs="-L$pkglibdir"
libs="$libs -lmysqlclient -lssl -lcrypto "
embedded_libs="-L$pkglibdir"
embedded_libs="$embedded_libs -l "
```
这样配置文件便修改完成.

也许你也会遇到其他问题,比如我遇到的"    error: command 'gcc' failed with exit status 1"
问题,解决mac上的缺少gcc的问题很简单,
3.gcc的安装
在终端窗口中,输入xcode-select --install:
```
$ xcode-select --install
```
会提示安装xcode-select插件,根据提示安装即可,安装成功后再次运行pip install mysqlclient就能顺利安装成功.

-----
20180912
#### 增加user模块流程：
- 1、新建user文件夹

&emsp;&emsp;一般都建在web/controllers（控制器文件夹下）
- 2、新建user.py文件，在文件中引入蓝图，并新建路由和函数
```python
from flask import Blueprint

route_user = Blueprint('user_page', __name__)  # 定义一个蓝图，参数包括页面名称和模块名


@route_user.route("/login")  # 定义蓝图的route访问的地址，定义login函数并返回login
def login():
    return "login"
```
- 3、在www.py文件中一定要注册user的路由，否则访问不了
```python
from web.controllers.user.User import route_user
app.register_blueprint( route_user, url_prefix = "/user" )

```
- render_template是渲染页面的模块
- flask默认的渲染页面是访问order下面的template，在本项目中，
渲染模块是放在web/controllers目录下，所以需要在application.py文件中修改渲染页面的
文件夹位置，修改__init__函数的参数，添加template_folder = None参数
然后将app变量的参数修改为：
```python
app=Application( __name__, template_folder=os.getcwd() + "/web/templates" )
```
这里的app变量中，参数制定了渲染文件的位置template_folder，其中os.getcwd指的是当前目录下也就order目录
既然用到os模块，就一定要import os
- 错误提示：
```python
jinja2.exceptions.UndefinedError: 'buildStaticUrl' is undefined
```
该错误提示是说明找不到静态文件

- common/libs下的UrlManager.py文件是链接管理器，静态文件的链接写到这里
比如buildStaticUrl，出现上诉错误的话，需要在application文件中添加函数模板

