from app import app
import os
from flask import send_from_directory, jsonify, request
from utils import auth

# MODELS
from models.Product import Product


@app.route('/test', methods=['GET'])
def get_tasks():
    print('yupi')
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