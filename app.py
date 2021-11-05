from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
from flask_cors import CORS

CORS(app)
# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://whereshallwemeet:sparta27@localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/posting')
def posting():
    return render_template('/page/posting_page.html')


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('/page/login_page.html', msg=msg)

@app.route('/lovesort')
def lovesort():
    card_list = list(db.post.find({}).sort("love", -1))
    print(card_list)
    print('POST방식')
    for card in card_list:
        card['_id'] = str(card['_id'])  ### html에서는 objectid형을 못읽기 때문에 str로 변환해서 보내준다
    return render_template('./page/main_page.html', card_list=card_list, sortType='좋아요순',title ='우리 어디서 만날까?')

@app.route('/')
def index():
    #print('GET방식')
    card_list = list(db.post.find({}))
    print(card_list)
    card_list.reverse()
    print(card_list)
    for card in card_list:
        card['_id'] = str(card['_id']) ### html에서는 objectid형을 못읽기 때문에 str로 변환해서 보내준다
    return render_template('./page/main_page.html', card_list=card_list, sortType='최신순', title ='우리 어디서 만날까?', cardType='all')

@app.route('/mypage/<userid>')
def mypage(userid):
    print(userid)
    print('GET방식')
    card_list = list(db.post.find({'userId': userid}))
    print(card_list)
    card_list.reverse()
    print(card_list)
    for card in card_list:
        card['_id'] = str(card['_id']) ### html에서는 objectid형을 못읽기 때문에 str로 변환해서 보내준다
    return render_template('./page/main_page.html', card_list=card_list, sortType='최신순', title ='나만의 장소', cardType ='my')



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)