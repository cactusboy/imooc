from flask import Flask, url_for
from imooc import route_imooc
from common.libs.UrlManager import UrlManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.register_blueprint(route_imooc, url_prefix = "/imooc")


app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///tmp/test.db'


@app.route('/')
def hello_world():
    url = url_for("index")
    url_1 = UrlManager.buildUrl("/api")
    return 'hello world, url:%s, url_1:%s'%(url, url_1)


@app.route("/api")
def index():
    return 'Index page'


@app.route("/api/heool")
def hello():
    return 'hello'


if __name__ == "__main__":
    app.run()
