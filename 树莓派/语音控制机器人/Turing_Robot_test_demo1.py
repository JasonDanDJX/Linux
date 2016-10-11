#测试图灵机器人
import numpy as np
from datetime import datetime
import wave
import urllib, urllib2, pycurl
import base64
import json
import os
import sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
print(sys.getdefaultencoding())
sys.setdefaultencoding("utf8")
print(sys.getdefaultencoding())

turing_key = '38b82b75ae7d4b0d8f17d89723d2e9a2'
turing_api = 'http://www.tuling123.com/openapi/api?key=' + turing_key + '&info='

def getHtml(url):
     page = urllib.urlopen(url)
     html = page.read()
     return html

info = "你叫什么名字"
request = turing_api + info
response = getHtml(request)
get_json = json.loads(response)
answer = get_json['text']

print(answer)
