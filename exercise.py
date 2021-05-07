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
    response["version"] = 1
    return jsonify(response), 200


@app.route('/user', methods=['GET'])
def user_list():
    if 'name' in request.args:
        n = request.args.get('name')
        found = []
        for user in users:
            if n.lower() in user.get('name').lower():
                found.append(user)
        return jsonify(found), 200
    else: 
        return jsonify(users), 200


@app.route('/user', methods=['POST'])
def user_create():
    req = request.get_json()
    user_name = req.get('name')
    user = dict(
        name = user_name
    )
    users.append(user)
    return jsonify({'message':'Added '+user_name}), 201


@app.route('/user', methods=['DELETE'])
def user_delete():
    req = request.get_json()
    user_name = req.get('name')
    user = dict(
        name = user_name
    )
    users.remove(user)
    return jsonify({'message':'Deleted '+user_name}), 200


@app.route('/')
def index():
    return render_template('welcome.html')
