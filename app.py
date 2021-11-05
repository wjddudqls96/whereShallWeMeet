from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('./loginPage/yb_login.html')


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('/loginPage/sytw/login.html', msg=msg)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
