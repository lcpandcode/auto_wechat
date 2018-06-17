# -*- coding: UTF-8 -*-
from flask import *
import threading
import wechat_core
wechat_instances = {}
app = Flask(__name__)

@app.route('/')
def hello_word():
    return "hello"

import itchat
def get_frinends_and_groups():
   instance = itchat.new_instance()
   instance.auto_login(picDir="./static/QR.png",loginCallback=after_login(instance))
   #返回二维码给前端
   return "登录成功!"

def after_login(instance):
    #登录完成，把对应微信的实例加入到一个字典中存储
    user = instance.get_friends()[0]
    user_name = user['UserName']
    global wechat_instances
    wechat_instances[user_name] = instance
import uuid
@app.route('/init')
def do_login():
    #线程执行后台微信相应程序
    num = uuid.uuid1()
    t = threading.Thread(target=get_frinends_and_groups())
    t.start()
    return "<html><body><img src='../static/QR.png'><div style>s%</div></body></html>"%(num)

@app.route('/friends')
def get_friends():
    friends_groups = wechat_core.get_friends_and_groups_list()
    for friend in friends_groups:
        print friend
    return friends_groups

if __name__=='__main__':
    app.run()