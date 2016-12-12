#!/usr/bin/env python
# encoding: utf-8
# time :  17:44
from flask import Flask,request,url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
# 修改http请求方法默认是get,使用参数methods改为post请求方法
@app.route('/user', methods=['POST'])
def hello_user():
    return 'Hello World'
# 请求时需要传递参数  http://127.0.0.1/user/121314
@app.route('/user/<id>')
def user_id(id):
    return 'Hello World: '+id

# 通过flask的request模块传递参数,请求地址http://127.0.0.1/qurey_user?id=123
@app.route('/qurey_user')
def qurey_user():
    id = request.args.get('id')
    return "qurey_user :" + id

# 反倒视图url,使用url_for模块  http://127.0.0.1/qurey_url
@app.route('/qurey_url')
def qurey_url():
    return "qurey url: "+url_for('qurey_user')
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=80,debug=True)