#!/usr/bin/env python
# encoding: utf-8
# 基本知识第二节
from flask import Flask,render_template
from models import User
app = Flask(__name__)


@app.route('/')
def hello_world():
    content = 'Hello World!'
    return render_template("index.html",content=content)

@app.route("/user")
def user_index():
    user=User(1,"songhailong")
    return render_template("user_index.html",user=user)
# 判断学习.传递参数进行判断,id是1的时候打印用户,不是则返回not this user http://127.0.0.1:5000/query_user/1
@app.route("/query_user/<user_id>")
def query_user(user_id):
    user=None
    if int(user_id) == 1:
        user = User(1,"songhailong")
    return render_template("user_id.html",user=user)
# 循环学习
@app.route("/users")
def user_list():
    users=[]
    for i in range(1,11):
        user=User(i,'WuTong'+str(i))
        users.append(user)
    return render_template("user_list.html",users=users)
# 模板继承
@app.route("/one")
def base_one():
    return render_template("base_one.html")
@app.route("/two")
def base_two():
    return render_template("base_two.html")

if __name__ == '__main__':
    app.run()
