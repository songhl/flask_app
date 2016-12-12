#!/usr/bin/env python
#coding:utf-8
#time: 2016/12/12 17:59
# 消息提示和异常处理
from flask import Flask,flash,render_template
app = Flask(__name__)
app.secret_key = '123'
@app.route("/")
def hello_world():
    flash("hello wutong")
    return render_template("index3.html")
if __name__ == '__main__':
    app.run()