import json

import flask
from bson import ObjectId
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/lovesort')
def lovesort():
    card_list = list(db.post.find({}).sort("love", -1))
    print(card_list)
    print('POST방식')
    for card in card_list:
        card['_id'] = str(card['_id'])  ### html에서는 objectid형을 못읽기 때문에 str로 변환해서 보내준다
    return render_template('./loginPage/yb/postDetailTest.html', card_list=card_list, sortType='좋아요순')

@app.route('/')
def index():
    print('GET방식')
    card_list = list(db.post.find({}))
    print(card_list)
    card_list.reverse()
    print(card_list)
    for card in card_list:
        card['_id'] = str(card['_id']) ### html에서는 objectid형을 못읽기 때문에 str로 변환해서 보내준다
    return render_template('./loginPage/yb/postDetailTest.html',card_list=card_list,sortType='최신순',title = '우리 어디서 만날까?',cardType='all')

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
    return render_template('./loginPage/yb/postDetailTest.html',card_list=card_list,sortType='최신순',title = '나만의 장소 저장소',cardType = 'my')


# @app.route('/postDetailPage/<data>')
# def postDetailShow(data):
#     print(json.loads(data))
#     jsonChangeData = json.loads(data)   ##url에서 받아온 data는 str형태기 때문에 json형변환을 해준다음 넣어준다
#
#     return render_template('./loginPage/yb/postDetailPage.html', postDetailData= jsonChangeData)

@app.route('/api/love',methods=['POST'])
def love():
    carId = request.form['carId']
    username = request.form['username']
    find_card =  list(db.post.find({'_id' : ObjectId(carId)})) ### 같은 id인 포스트를 찾아온다
    find_card_love = find_card[0]['love'] #찾은 포스트의 좋아요 개수
    loveClickUsers = find_card[0]['loveClickUsers'] #찾은 포스트의 좋아요를 누른 사람들
    loveClickUsers.append(username)  #좋아요를 누른 리스트에 집어넣고
    db.post.update_one({'_id': ObjectId(carId)}, {'$set': {'love': find_card_love + 1,'loveClickUsers' :loveClickUsers}}) # 해당 포스트를 업데이트 시켜준다
    return jsonify({'success': True})

@app.route('/api/loveCancle',methods=['POST'])
def loveCancle():
    carId = request.form['carId']
    username = request.form['username']
    find_card = list(db.post.find({'_id': ObjectId(carId)}))  ### 같은 id인 포스트를 찾아온다
    find_card_love = find_card[0]['love']  # 찾은 포스트의 좋아요 개수
    loveClickUsers = find_card[0]['loveClickUsers']  # 찾은 포스트의 좋아요를 누른 사람들
    loveClickUsers.remove(username)
    db.post.update_one({'_id': ObjectId(carId)},{'$set': {'love': find_card_love - 1, 'loveClickUsers': loveClickUsers}})  # 해당 포스트를 업데이트 시켜준다
    return jsonify({'success': False})

@app.route('/api/deletePost',methods=['POST'])
def deletePost():
    carId = request.form['carId']
    db.post.delete_one({'_id': ObjectId(carId)})
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)