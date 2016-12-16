#!/usr/bin/env python
#coding:utf-8
#time: 2016/12/12 17:59
from flask import Flask,flash,render_template,request
app = Flask(__name__)
app.secret_key = '123'
@app.route("/")
def hello_world():
    flash("hello wutong")
    return render_template("index3.html")
@app.route("/login",methods=["POST","GET"])
def login():
    form =request.form
    username=form.get("username")
    password=form.get("password")
    if not username:
        flash("please input username")
        return render_template("index3.html")
    if not password:
        flash("please input password")
        return render_template("index3.html")
    if username == "songhailong" and password == "hailong":
        flash("login success")
        return render_template("index3.html")
    else:
        flash("username or password is wrong")
        return render_template("index3.html")
if __name__ == '__main__':
    app.run()