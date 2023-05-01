import os 

from flask import Flask, jsonify



app = Flask(__name__)

@app.route('/')
def hello_world():
    my_env = os.getenv('FLASK_ENV')
    return jsonify({'env': my_env})
