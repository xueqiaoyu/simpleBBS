"""
@author:xue
@file:view.py
@time:2019/7/19 下午5:17
"""

from flask import Blueprint,render_template

bp = Blueprint('front',__name__)

@bp.route('/')
def hello_world():
    return render_template('front/index.html')

