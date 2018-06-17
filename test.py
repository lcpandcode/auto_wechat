# -*- coding: UTF-8 -*-
import threading
import time
def t1():
    time.sleep(1)
    print "t1 end"

threading.Thread(target=t1)
