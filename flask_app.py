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

if __name__ == '__main__':
    app.run()
