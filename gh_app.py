from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

from datetime import datetime

@app.route('/posting')
def home():
    return render_template('/loginPage/gh/index_kgh.html')

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
        'title':title_receive,
        'content':content_receive,
        'address':address_receive,
        'location': location_receive,
        'imgFile': f'{filename}.{extension}',
        'time': today.strftime('%Y.%m.%d'),
        'userId' : userid_receive,
        'nickName' : nickname_receive,
        'loveClickUsers': [],
        'love' : 0

    }

    db.post.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=4000, debug=True)