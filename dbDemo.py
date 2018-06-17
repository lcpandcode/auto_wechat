# -*- coding: UTF-8 -*-
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='wechat')
cur = conn.cursor()
cur.execute("SELECT * FROM user_friends")
print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()