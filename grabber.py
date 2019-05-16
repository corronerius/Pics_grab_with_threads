#!/usr/bin/env python
# coding: utf-8

from io import BytesIO
import requests
import urllib
import numpy as np
import string 
import secrets
import threading 
import time


url = 'https://picsum.photos/256/256'
char_set = string.ascii_uppercase + string.digits
interval = 1
x = 10


class GrabThread(threading.Thread):
    def __init__(self,interval):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval
    def run(self):
        for i in range (x):
            img_from_web = open('/home/andrii/parse/pic{}.jpg'.format(''.join((secrets.choice(char_set) for _ in range (6)))),'xb')
            img_from_web.write(requests.get(url).content)
            img_from_web.close()
            time.sleep(interval)

            
def create_threads():
      for i in range(5):
        name = "Thread #%s" % (i+1)
        my_thread = GrabThread(name)
        my_thread.start()
        my_thread.join()
        
if __name__ == "__main__":
    create_threads()
