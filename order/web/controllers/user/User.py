from flask import Blueprint, render_template  # render_template是渲染页面的模块
from common.libs.UrlManager import UrlManager
route_user = Blueprint('user_page', __name__)  # 定义一个蓝图，参数包括页面名称和模块名


@route_user.route("/login")  # 定义蓝图的route访问的地址，定义login函数并返回login
def login():
    return render_template("user/login.html")
