"""
@author:xue
@file:views.py
@time:2019/7/19 下午5:14
"""
from flask import Blueprint,views,render_template

bp = Blueprint('cms',__name__,url_prefix='/cms')

class LogininView(views.MethodView):
    def get(self):
        pass

    def post(self):
        pass

