# -*- coding: UTF-8 -*-
import itchat
import httplib
import json



@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

    requrl = "http://www.tuling123.com/openapi/api?key=778aa7e1f3144489abbf3d4be672a3cb&info=%s" % (msg.text)
    headerdata = {"Host": "47.94.75.128"}

    conn = httplib.HTTPConnection("47.94.75.128")

    conn.request(method="GET", url=requrl, headers=headerdata)

    response = conn.getresponse()

    res = response.read()
    print res

    result = json.loads(res)
    print result['text']
    return result['text']


itchat.auto_login()
itchat.run()