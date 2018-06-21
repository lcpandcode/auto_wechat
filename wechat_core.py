# -*- coding: UTF-8 -*-
#微信交互核心模块
import itchat

def get_friends_and_groups_list(chat_instance):
    #获取friends
    friends_groups = {}
    friends_groups['friends'] = chat_instance.get_friends()
    friends_groups['rooms'] = chat_instance.get_chatrooms()
    return friends_groups

