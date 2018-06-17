# -*- coding: UTF-8 -*-
from flask import *
import threading
app = Flask(__name__)

@app.route('/')
def hello_word():
    return "hello"



@app.route('/auto_replay_friends_list')
def do_login():
    return request.args.get("friends")
if __name__=='__main__':
    app.run()