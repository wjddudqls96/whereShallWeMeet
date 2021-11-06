from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
from flask_cors import CORS

CORS(app)  #통신 부분에서 cors 에러가 생겨 flask_cors 라이브러리를 설치한뒤에 cors오류 해결
# client = MongoClient('localhost', 27017)
client = MongoClient('localhost', 27017)
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
    card_list = list(db.post.find({}).sort("love", -1))  #좋아요 수로 정렬하여 card_list에 저장한다.
    print('POST방식')
    for card in card_list:
        card['_id'] = str(card['_id'])  ### html에서는 objectid형을 못읽기 때문에 str로 변환해서 보내준다
    return render_template('./page/main_page.html', card_list=card_list, sortType='좋아요순',title ='우리 어디서 만날까?', cardType='all')

@app.route('/') #whereshallwemeet의 main페이지 render_template부분입니다.
def index():
    #print('GET방식')
    card_list = list(db.post.find({}))   #post에 있는 모든 데이터를 card_list에 저장합니다.
    card_list.reverse()  #최신순으로 출력하기위해 card_list를 reverse해줍니다.
    for card in card_list:
        card['_id'] = str(card['_id']) ### html에서는 objectid형을 못읽기 때문에 str로 변환해서 card['id']에 저장합니다.
    return render_template('./page/main_page.html', card_list=card_list, sortType='최신순', title ='우리 어디서 만날까?', cardType='all')

@app.route('/mypage/<userid>')
def mypage(userid):
    card_list = list(db.post.find({'userId': userid}))  #사용자의 만든 카드를 불러온다.
    card_list.reverse() # 최신순으로 바꾼다.
    for card in card_list:
        card['_id'] = str(card['_id']) ### html에서는 objectid형을 못읽기 때문에 str로 변환해서 보내준다
    return render_template('./page/main_page.html', card_list=card_list, sortType='최신순', title ='나만의 장소', cardType ='my')



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)