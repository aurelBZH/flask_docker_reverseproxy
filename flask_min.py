# /usr/bin/env python 3.5
# coding: utf-8

from flask import Flask, Blueprint

flask_min = Blueprint("flask_min", __name__)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(flask_min)
    return app

@flask_min.route('/')
def hello_world():
    
    return 'Flask test'


