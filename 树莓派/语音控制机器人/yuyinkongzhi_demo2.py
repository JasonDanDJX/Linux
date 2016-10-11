#加入调用浏览器
import numpy as np
from datetime import datetime
import wave
import urllib, urllib2, pycurl
import base64
import json
import os
import sys
import re
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
#print(sys.getdefaultencoding())#调试监测用
sys.setdefaultencoding("utf8")
#print(sys.getdefaultencoding())#调试监测用


filename = '/home/pi/Desktop/voice_files/test.wav'#录音文件，注意保存路径
dialogue = '0'
apiKey = "hd5irhISgaQL6kGaSkHGGQ9z"
secretKey = "ae65403e214557fc4ea21fd84b58d561"
auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;
cuid = "8642936"
#用户私有，需注册
turing_key = '38b82b75ae7d4b0d8f17d89723d2e9a2'
turing_api = 'http://www.tuling123.com/openapi/api?key=' + turing_key + '&info='
#上面是图灵机器人
def getHtml(url):
     page = urllib.urlopen(url)
     html = page.read()
     return html


def get_token():
     res = urllib2.urlopen(auth_url)
     json_data = res.read()
     return json.loads(json_data)['access_token']


def dump_res(buf):
     global dialogue
     print (buf)
     a = eval(buf)
     #print type(a)
     if a['err_msg']=='success.':
          dialogue = a['result'][0]#返回识别结果
          print ("我："+dialogue)


def use_cloud(token):#上传百度语音识别
     fp = wave.open(filename, 'rb')#调用录音文件
     nf = fp.getnframes()
     f_len = nf * 2
     audio_data = fp.readframes(nf)
     srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
     http_header = [
        'Content-Type: audio/wav; rate=16000',#注意设置文件格式（wav）和频率（16000）
        'Content-Length: %d' % f_len
        ]
     c = pycurl.Curl()
     c.setopt(pycurl.URL, str(srv_url)) #curl doesn't support unicode
     c.setopt(c.HTTPHEADER, http_header)   #must be list, not dict
     c.setopt(c.POST, 1)
     c.setopt(c.CONNECTTIMEOUT, 30)
     c.setopt(c.TIMEOUT, 30)
     c.setopt(c.WRITEFUNCTION, dump_res)
     c.setopt(c.POSTFIELDS, audio_data)
     c.setopt(c.POSTFIELDSIZE, f_len)
     c.perform() #pycurl.perform() has no return val



def TTS(mesg):#语音合成
     upload_answer = mesg.encode("utf8")
     #print type(upload_answer)#调试监测用 
     url = "http://tsn.baidu.com/text2audio?tex="+upload_answer+"&lan=zh&per=0&pit=5&spd=7&cuid="+cuid+"&ctp=1&tok="+token#这是语音合成，查询API文档：）
     #print(url)#调试监测用 
     os.system('mplayer "%s"'%(url))

def TuringRobot():
     info = dialogue
     request = turing_api + info
     response = getHtml(request)
     get_json = json.loads(response)
     print (get_json)
     answer = get_json['text']
     print("机器人："+answer)
     TTS(answer)
     
while(True):
     print("请说话...")
     os.system('arecord -d 5 -r 16000 -c 1 -t wav -f S16_LE -D plughw:1,0 '+filename)#相关指令查询录音指令文档：）
     print("完毕！")
     token = get_token()
     #print("token="+token)
     #获得token
     use_cloud(token)
     #进行识别处理，然后人机交互
     if dialogue != '0':
          if re.search('结束',dialogue) :
               answer = '我是小玲，感谢使用，再会'
               print("机器人："+answer)
               #print type(answer)#调试监测用
               TTS(answer)
               break
          elif (re.search('开',dialogue) or re.search('暗',dialogue) or re.search('看不见',dialogue)):
               answer = '好的，正在帮您开灯。。。'
               print("机器人："+answer)
               #print type(answer)#调试监测用
               TTS(answer)
               os.system('cd /home/pi/Program/LED&&sudo ./ledON')
               dialogue = '0'
          elif (re.search('关',dialogue) or re.search('亮',dialogue) or re.search('刺眼',dialogue)) :
               answer = '好的，正在帮您关灯。。。'
               print("机器人："+answer)
               #print type(answer)#调试监测用
               TTS(answer)
               os.system('cd /home/pi/Program/LED&&sudo ./ledOFF')
               dialogue = '0'
          elif re.search('闪' ,dialogue) :
               answer = '开始闪烁。。。'
               print("机器人："+answer)
               #print type(answer)#调试监测用
               TTS(answer)
               os.system('cd /home/pi/Program/blink_test/&&sudo ./blink_test')
               dialogue = '0'
          else:
               TuringRobot()  
               dialogue = '0'
     else:
          continue
        
        
        
    

