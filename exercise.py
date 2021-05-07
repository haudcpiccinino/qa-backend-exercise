from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/info', methods=['GET'])
def respond():
    response = {}
    response["version"] = 1
    return jsonify(response)

@app.route('/')
def index():
    return "<h1>Welcome to our server</h1>"
