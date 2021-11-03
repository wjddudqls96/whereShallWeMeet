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
    userNickname = request.form['nickName']
    find_card =  list(db.test.find({'_id' : ObjectId(carId)})) ### 같은 id인 포스트를 찾아온다
    find_card_love = find_card[0]['love'] #찾은 포스트의 좋아요 개수
    loveClickUsers = find_card[0]['loveClickUsers'] #찾은 포스트의 좋아요를 누른 사람들
    if userNickname not in loveClickUsers:  #만약 좋아요를 처음 누른 사람이라면
        print("좋아요 처음 눌렸어요.")
        loveClickUsers.append(userNickname)  #좋아요를 누른 리스트에 집어넣고
        db.test.update_one({'_id': ObjectId(carId)}, {'$set': {'love': find_card_love + 1,'loveClickUsers' :loveClickUsers}}) # 해당 포스트를 업데이트 시켜준다
        return jsonify({'success': True})
    else:                                   #만약 좋아요를 전에 눌렀던 사람이라면
        print("이미 좋아요를 누룬사람입니다.")
        return jsonify({'success': False})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)