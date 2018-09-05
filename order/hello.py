from flask import Flask
from imooc import route_imooc

app = Flask(__name__)
app.register_blueprint(route_imooc, url_prefix = "/imooc")


@app.route('/')
def hello_world():
    return 'hello world'


@app.route("/api")
def index():
    return 'Index page'


@app.route("/api/heool")
def hello():
    return 'hello'


if __name__ == "__main__":
    app.run()
