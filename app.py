import os
import dataset
from flask import Flask, send_from_directory, jsonify, request

db = dataset.connect('sqlite:///mydb')

from utils import auth
import json



app = Flask(__name__, static_folder='client/build')

# MODELS
from models.Product import Product

@app.route('/login', methods=['POST'])
def valid_login():
    data = json.loads(request.data)
    user = data['user']
    password = data['password']
    token = auth.login(user, password)
    if token != False:
        return jsonify({'ok': str(token) })
    else:
        return jsonify({'ok': 'none'})
    

    

@app.route('/test', methods=['GET', 'POST'])
def get_tasks():
    token = request.headers.get('token')
    if auth.is_auth(token):
        return jsonify({'tasks': 'all'})
    else:
        return jsonify({'tasks': 'none'})

@app.route('/user/test')
def user_test():
    np = Product('novo', 0, 0, 0)
    np.save()


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("client/build/" + path):
        return send_from_directory('client/build', path)
    else:
        return send_from_directory('client/build', 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

