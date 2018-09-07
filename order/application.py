from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager


class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        # 基础环境
        self.config.from_pyfile('config/base_setting.py')

        # 本地环境
        self.config.from_pyfile('config/local_setting.py')

        # 生产环境
        self.config.from_pyfile('config/production_setting.py')

        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)
manager = Manager( app )
