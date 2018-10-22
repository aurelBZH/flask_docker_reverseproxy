# /usr/bin/env python 3.5
# coding: utf-8

import flask_min as fmin

app = fmin.create_app()


if __name__ == '__main__':
    app.run("0.0.0.0")
    