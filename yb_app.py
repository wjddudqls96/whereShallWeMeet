import json

from bson import ObjectId
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def login():
    card_list = list(db.test.find({}))
    print(card_list)
    for card in card_list:
        card['_id'] = str(card['_id']) ### html에서는 objectid형을 못읽기 때문에 str로 변환해서 보내준다
    return render_template('./loginPage/yb/postDetailTest.html',card_list=card_list)


# @app.route('/postDetailPage/<data>')
# def postDetailShow(data):
#     print(json.loads(data))
#     jsonChangeData = json.loads(data)   ##url에서 받아온 data는 str형태기 때문에 json형변환을 해준다음 넣어준다
#
#     return render_template('./loginPage/yb/postDetailPage.html', postDetailData= jsonChangeData)

@app.route('/api/love',methods=['POST'])
def love():
    carId = request.form['carId']
    print(carId)
    find_card =  list(db.test.find({'_id' : ObjectId(carId)}))
    print(find_card)
    find_card_love = find_card[0]['love']
    db.test.update_one({'_id': ObjectId(carId)}, {'$set': {'love': find_card_love+1}})
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)