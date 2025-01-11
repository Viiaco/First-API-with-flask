from flask import jsonify
from app import app, auth

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/login', methods=['GET'])
@auth.login_required 
def login():
    username = format(auth.current_user())
    return jsonify({"message": "Hello: " + username })