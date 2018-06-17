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
def login(uunum):
   instance = itchat.new_instance()
   instance.auto_login(picDir="/home/lcp/PycharmProjects/auto_wechat/static/QR.png")
   # 登录完成，把对应微信的实例加入到一个字典中存储
   global wechat_instances
   wechat_instances[uunum] = instance


import uuid
#初始化：微信二维码等信息
@app.route('/init')
def init():
    #线程执行后台微信相应程序
    num = uuid.uuid1()
    t = threading.Thread(target=login,args=(num))
    t.start()
    return render_template("main.html",uuid_num=num)

@app.route('/friends')
def get_friends():
    uuid = request.args.get("uuid")
    instance = wechat_instances[uuid]
    friends_groups = wechat_core.get_friends_and_groups_list(instance)
    for friend in friends_groups:
        print friend
    return friends_groups


if __name__=='__main__':
    app.run()