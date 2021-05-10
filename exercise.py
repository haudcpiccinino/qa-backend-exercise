import os
from lib.db import Database
from flask import Flask, request, jsonify, render_template

version = 'n/a'
if 'APP_VERSION' in os.environ:
    version = os.environ['APP_VERSION']

db_host = '127.0.0.1'
if 'DB_HOST' in os.environ:
    db_host = os.environ['DB_HOST']

db_name = 'postgres'
if 'DB_NAME' in os.environ:
    db_name = os.environ['DB_NAME']

db_pass = 'password'
if 'DB_PASS' in os.environ:
    db_pass = os.environ['DB_PASS']

db_port = 5432
if 'DB_PORT' in os.environ:
    db_port = os.environ['DB_PORT']

db_user = 'admin'
if 'DB_USER' in os.environ:
    db_user = os.environ['DB_USER']

db = Database(host=db_host, dbname=db_name, password=db_pass, port=db_port, user=db_user);


app = Flask(__name__)


@app.route('/info', methods=['GET'])
def respond():
    response = {}
    response = {
        'version': version
    }
    return jsonify(response), 200


@app.route('/user', methods=['GET'])
def user_list():
    try:
        users = []
        if 'name' in request.args:
            name = request.args.get('name')
            users = db.users_list(name)
            return jsonify(users), 200
        else:
            db_users = db.users_list()

            for db_user in db_users:
                users.append(dict(
                    id = db_user[0],
                    name = db_user[1],
                    occupation = db_user[2]
                ))

            return jsonify(users), 200

    except Exception as e:
        return jsonify({ 'error': str(e) }), 400


@app.route('/user', methods=['POST'])
def user_create():
    try:
        req = request.get_json()
        name = ''
        occupation = ''
        
        if 'name' in req:
            name = req.get('name')
        
        if 'occupation' in req:
            occupation = req.get('occupation')
        
        if len(name) == 0 or len(occupation) == 0:
            return jsonify({ 'error': 'Name and Occupation properties are required.' }), 400
        else:
            db_id = db.users_add(name,occupation)
            return jsonify({'message':'User `{}` added.'.format(name)}), 201

    except Exception as e:
        return jsonify({ 'error': str(e) }), 400


@app.route('/user', methods=['DELETE'])
def user_delete():
    try:
        req = request.get_json()
        if 'name' in req:
            name = req.get('name')
            db.users_remove(name)
            return jsonify({'message':'User `{}` is removed.'.format(name)}), 200
        return jsonify({ 'error': 'Name property is required.' }), 400
    except Exception as e:
        return jsonify({ 'error': str(e) }), 400


@app.route('/')
def index():
    return render_template('welcome.html')
