# -*- coding: UTF-8 -*-
import threading
import time
def test1():
    aa = 1
    aa = aa +1
str = u'\u9648\u60e0\u971e'.encode('utf-8')
test1()
str2 = 'A'
str2 = str2.encode('utf-8')
print str2
arr = ['a','b']
arr2 = ['c','d']
arr.append(arr2)
for i in arr:
    print i
