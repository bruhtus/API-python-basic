import json
import os
import pymongo
from flask import Flask, Response, jsonify
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://bruhtus:insert_password_here@cluster0.chq4a.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client['mongodb_basic']

@app.route('/api/v1.0/students', methods=['GET'])
def students():
    '''student_list = [
            {
                'name':'Robertus',
                'country':'Indonesia',
                'city':'Surabaya',
                'skills':['Linux shell', 'Python', 'Adobe lightroom']
            },
            {
                'name':'Anu',
                'country':'UK',
                'city':'London',
                'skills':['Python','Mongodb']
            },
            {
                'name':'Itu',
                'country':'Sweden',
                'city':'Stockholm',
                'Skills':['Java','C#']
            }
            ]'''
    all_students = db.students.find()
    response = []
    for student in all_students:
        student['_id'] = str(student['_id'])
        response.append(student)
    #return Response(json.dumps(student_list), mimetype='application/json')
    return jsonify(response)

@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    name = request.form['name']
    country = request.form['country']
    city = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
            'name': name,
            'country': country,
            'city': birthyear,
            'skills': skills,
            'bio': bio,
            'created_at': created_at,
            }

    return db.students.insert_one(student)

@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    student = db.students.find({'_id':ObjectId('5fbb134afbdec51ce5600497')})
    return Response(dumps(student), mimetype='application/json') #doesn't display in json format for some reason

@app.route('/api/v1.0/students/<id>', methods=['POST'])
def update_student(id):
    query = {'_id':ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
            'name': name,
            'country': country,
            'city': birthyear,
            'skills': skills,
            'bio': bio,
            'created_at': created_at,
            }

    return db.students.update_one(query, student)

@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    return db.students.delete_one({'_id':ObjectId(id)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
