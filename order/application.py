from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager


import os
class Application(Flask):
    def __init__(self, import_name, template_folder = None,root_path = None):  # 默认渲染文件夹为None,route_path是静态文件的位置
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path = root_path, static_folder=None)
        """template_folder=template_folder是将渲染文件夹的值传入进来,
        并且把flask默认的static文件夹设置为None：“static_folder=None”
        """
        # 基础环境
        self.config.from_pyfile('config/base_setting.py')

        # 本地环境
        self.config.from_pyfile('config/local_setting.py')

        # 生产环境
        self.config.from_pyfile('config/production_setting.py')

        db.init_app(self)


db = SQLAlchemy()
app = Application( __name__ ,template_folder = os.getcwd() + "/web/templates/", root_path=os.getcwd() ) # 制定渲染文件夹
manager = Manager( app )

'''
函数模板
'''
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl,'buildUrl')
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')