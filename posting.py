import json

import flask
from bson import ObjectId
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient

from datetime import datetime
from flask_cors import CORS

#client = MongoClient('localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta


CORS(app) #통신 부분에서 cors 에러가 생겨 flask_cors 라이브러리를 설치한뒤에 cors오류 해결

@app.route('/api/love',methods=['POST'])
def love():
    carId = request.form['carId']
    username = request.form['username']
    find_card =  list(db.post.find({'_id' : ObjectId(carId)})) ### 같은 id인 포스트를 찾아온다
    find_card_love = find_card[0]['love'] #찾은 포스트의 좋아요 개수
    loveClickUsers = find_card[0]['loveClickUsers'] #찾은 포스트의 좋아요를 누른 사람들
    loveClickUsers.append(username)  #좋아요를 누른 리스트에 집어넣고
    db.post.update_one({'_id': ObjectId(carId)}, {'$set': {'love': find_card_love + 1,'loveClickUsers' :loveClickUsers}}) # 해당 포스트를 업데이트 한다.
    return jsonify({'success': True})

@app.route('/api/loveCancle',methods=['POST'])
def loveCancle():
    carId = request.form['carId']
    username = request.form['username']
    find_card = list(db.post.find({'_id': ObjectId(carId)}))  ### 같은 id인 포스트를 찾아온다
    find_card_love = find_card[0]['love']  # 찾은 포스트의 좋아요 개수
    loveClickUsers = find_card[0]['loveClickUsers']  # 찾은 포스트의 좋아요를 누른 사람들
    loveClickUsers.remove(username) #좋아요를 누른 사람들의 리스트에서 username과 같은 인덱스를 삭제한다.
    db.post.update_one({'_id': ObjectId(carId)},{'$set': {'love': find_card_love - 1, 'loveClickUsers': loveClickUsers}})  # 해당 포스트를 업데이트 시켜준다
    return jsonify({'success': False})

@app.route('/api/deletePost',methods=['POST'])
def deletePost():
    carId = request.form['carId']
    db.post.delete_one({'_id': ObjectId(carId)})   #해당 되는 id의 카드를 삭제한다.
    return jsonify({'success': True})


@app.route('/diary', methods=['POST'])
def save_diary():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    address_receive = request.form['address_give']
    location_receive = request.form['location_give']
    nickname_receive = request.form['nickname_give']
    userid_receive = request.form['userid_give']
    file = request.files["file_give"]

    location_receive = location_receive.split(',')
    location_receive[0] = float(location_receive[0])
    location_receive[1] = float(location_receive[1])
    print(location_receive)
    print(type(location_receive[0]))
    extension = file.filename.split('.')[-1]

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'file-{mytime}'

    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'title': title_receive,
        'content': content_receive,
        'address': address_receive,
        'location': location_receive,
        'imgFile': f'{filename}.{extension}',
        'time': today.strftime('%Y.%m.%d'),
        'userId': userid_receive,
        'nickName': nickname_receive,
        'loveClickUsers': [],
        'love': 0

    }

    db.post.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=4000, debug=True)