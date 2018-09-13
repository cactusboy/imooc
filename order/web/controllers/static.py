from flask import Blueprint, send_from_directory # send_from_directory是加载资源的模块
from application import app

'''
本文件主要是为了在开发环境中能正常访问静态文件，
'''
route_static = Blueprint('static', __name__)
@route_static.route("/<path:filename>")
def index( filename ):
    return send_from_directory( app.root_path + "/web/static/", filename )