# -*- coding: UTF-8 -*-
from flask import *
import threading
import wechat_core
import util
user_instances = {}
app = Flask(__name__)
#User类：用于记录用户状态：包括微信是否登录成功，对应的微信实例等等信息
class User:
     uunum = ''
     wechat_instance = None
     wechat_login = False #是否登录了微信
     sys_login = False #是否登录了平台
     user_id = -1
     auto_reply_friends = []
@app.route('/')
def hello_word():
    response = make_response("test")
    response.set_cookie('name','test')
    return response

import itchat
def login(user):
   instance = user.wechat_instance
   instance.auto_login(picDir="/home/lcp/PycharmProjects/auto_wechat/static/%s.png" % (user.uunum),)

import uuid
#初始化：微信二维码等信息
@app.route('/init')
def init():
    #线程执行后台微信相应程序
    num = str(uuid.uuid1())
    user = User()
    user.uunum = num
    user.wechat_instance = itchat.new_instance()
    global user_instances
    user_instances[num] = user
    t = threading.Thread(target=login,args=(user,))
    t.start()
    response = make_response(render_template("qr.html", uuid_num=num))
    response.set_cookie('uuid',num)
    return response

@app.route('/friends')
def get_friends():
    #uuid = request.args.get("uuid")
    uuid = request.cookies.get('uuid')
    global user_instances
    wechat_instance = user_instances[uuid].wechat_instance
    friends_groups = wechat_core.get_friends_and_groups_list(chat_instance=wechat_instance)
    friends = []
    for friend in friends_groups['friends']:
        tem = friend['RemarkName']
        if tem==None or tem=='':
            tem = friend['NickName']
        tem.encode('utf-8')
        friends.append(tem)
    rooms = []
    for room in friends_groups['rooms']:
        rooms.append(room['NickName'])
    return util.json_get(True,render_template("friends.html",friends=friends,rooms=rooms))
@app.route('/auto_reply_setting')
def auto_reply_setting():
    friends_str = request.args.get("friends")
    friends = json.loads(friends_str)
    uunum = request.cookies.get('uuid')
    global user_instances
    instance = user_instances[uunum]
    for i in friends:
        if(i not in instance.auto_reply_friends):
            instance.auto_reply_friends.append(i)

    print friends_str
    return friends_str;

@app.route('/register_template')
def register_template():
    return render_template("register.html")

@app.route('/login_template')
def login_template():
    return render_template("login.html")

@app.route('/forget_password_template')
def forget_password_template():
    return render_template("forget_password.html")
if __name__=='__main__':
    app.run()






