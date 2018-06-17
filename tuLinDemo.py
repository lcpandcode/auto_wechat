# -*- coding: UTF-8 -*-
#调用图灵机器人接口demo
import urllib
import httplib
import json

def getMsg(msg):
    requrl = "http://www.tuling123.com/openapi/api?key=778aa7e1f3144489abbf3d4be672a3cb&info=%s" % (msg)
    headerdata = {"Host": "47.94.75.128"}

    conn = httplib.HTTPConnection("47.94.75.128")

    conn.request(method="GET", url=requrl, headers=headerdata)

    response = conn.getresponse()

    res = response.read()

    result = json.loads(res)
    print result['text']
    return result['text']

getMsg("哈哈")