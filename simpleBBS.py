"""
@author:xue
@file:simpleBBS.py
@time:2019/7/19 下午5:06
"""

from flask import Flask,render_template
from apps.cms.views import bp as cms_bp
from apps.common.views import bp as common_bp
from apps.front.views import bp as front_bp
import config

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(cms_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)

if __name__ == '__main__':
    app.run(port=8888)