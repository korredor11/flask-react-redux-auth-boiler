from app import db
import hashlib
import datetime

users = db['users']
tokens = db['tokens']

def is_auth(token):
    if token == '123':
        return True
    else:
        return False

def login(user, password):
    if users.find_one(user=user):
        user = users.find_one(user=user)
        print('user: ', user)
        if user['password'] == password:
            exp = datetime.datetime.now() + datetime.timedelta(minutes=15)
            token_str = str(user['user']) + str(user['password']) + str(datetime.datetime.now())
            token = hashlib.md5(token_str.encode()).hexdigest()
            tokens.insert(dict(token=token, exp=exp))
            return token
        else:
            return False
    else:
        return False