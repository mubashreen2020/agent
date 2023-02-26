from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/users')
def users():
    return 'List of users'
export FLASK_APP=app.py
flask run --host=192.168.1.8
