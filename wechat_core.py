# -*- coding: UTF-8 -*-
#微信交互核心模块
import itchat

def get_friends_and_groups_list(chat_instance):
    #获取friends
    friends = chat_instance.get_friends()
    for friend in friends:
        name = friend['RemarkName']
        if name == None or name == "":
            name = friend['NickName']
        print name