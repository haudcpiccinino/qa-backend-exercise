import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

users = [
    dict (
        name = "Dorothy Gale"
    )
]


@app.route('/info', methods=['GET'])
def respond():
    response = {}
    if 'APP_TEST_VAR' in os.environ:
        response["version"] = os.environ['APP_VERSION']
    else:
        response["version"] = 'n/a'
    return jsonify(response), 200


@app.route('/user', methods=['GET'])
def user_list():
    if 'name' in request.args:
        try:
            n = request.args.get('name')
            found = []
            for user in users:
                if n.lower() in user.get('name').lower():
                    found.append(user)
            return jsonify(found), 200
        except:
            return jsonify({'message':'Something went wrong. Users cannot be listed.'}), 400
    else:
        return jsonify(users), 200


@app.route('/user', methods=['POST'])
def user_create():
    req = request.get_json()
    user_name = req.get('name')
    user = dict(
        name = user_name
    )
    try:
        users.append(user)
        return jsonify({'message':'Added '+user_name}), 201
    except:
        return jsonify({'message':'Something went wrong. User '+user_name+' was not added'}), 400




@app.route('/user', methods=['DELETE'])
def user_delete():
    req = request.get_json()
    user_name = req.get('name')
    user = dict(
        name = user_name
    )
    try:
        users.remove(user)
        return jsonify({'message':'Removed '+ user_name}), 200
    except:
        return jsonify({'message':'Something went wrong. User '+ user_name+' was not removed.'}), 400



@app.route('/')
def index():
    return render_template('welcome.html')
