from flask import jsonify, request, json
from flask_httpauth import HTTPBasicAuth
from passlib.hash import sha256_crypt

from app import app, db
from models import User

auth = HTTPBasicAuth()


@app.route('/todo/api/v1.0/users', methods=['POST'])
def create_user():
    user = User(username=request.json['username'], email=request.json['email'], password_hash= sha256_crypt.encrypt(request.json['password']))
    db.session.add(user)
    db.session.commit()
    return jsonify({'user created': str(user)})


@app.route('/todo/api/v1.0/users', methods=['GET'])
def get_users():
    query = db.session.query(User)
    return json.dumps(query.all())


@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None