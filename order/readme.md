#### 20180909
### mac下安装mysqlclient模块的注意事项
由于需要在mac下配置python3的开发环境,需要安装flask和mysqlclient,在虚拟环境下安装mysqlclient出错,
于是记录下踩坑过程:
1:在mac下的python3.7的虚拟环境中安装mysqlclient时出错:
" OSError: mysql_config not found"
原因是没有安装mysql的配置模块"mysql-connector-c"
打开一个终端窗口,安装mysql-sonnector-c
'''
$ brew install mysql-connector-c
'''
安装完成后,运行pip install mysqlclient还是会出错,因为mysql_config文件还没有配置(出于官方的原因,需要手动修改mysql_config文件才能正确安装)
2,修改mysql_config文件
进入配置文件所在目录
'''
$ cd /usr/local/cellar/mysql-connector-c/6.1.11/bin
'''
其中:6.1.11是版本目录,根据自己安装的版本会有变动.
使用vim编辑mysql_config文件,在第112行附近代码如下:
'''
# Create options
libs="-L$pkglibdir"
libs="$libs -l "
embedded_libs="-L$pkglibdir"
embedded_libs="$embedded_libs -l "
'''
将(libs="$libs -l -lssl -lcrypto ")改成
(libs="$libs -lmysqlclient -lssl -lcrypto ")
如下图:
'''
# Create options
libs="-L$pkglibdir"
libs="$libs -lmysqlclient -lssl -lcrypto "
embedded_libs="-L$pkglibdir"
embedded_libs="$embedded_libs -l "
'''
这样配置文件便修改完成.

也许你也会遇到其他问题,比如我遇到的"    error: command 'gcc' failed with exit status 1"
问题,解决mac上的缺少gcc的问题很简单,
3.gcc的安装
在终端窗口中,输入xcode-select --install:
'''
$ xcode-select --install
'''
会提示安装xcode-select插件,根据提示安装即可,安装成功后再次运行pip install mysqlclient就能顺利安装成功.
