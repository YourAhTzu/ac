''' 
@阿慈
垃圾毛自己玩吧
入口：https://wx.qrurl.net/?t=231005dD57Uv
new Env('垃圾毛'); 
www.rroadem.cn域名内的session_id填入qtjt变量中
'''
import os
import requests

url = 'https://www.rroadem.cn/?s=/ApiRewardVideoAd/givereward&aid=3&platform=wx&session_id=' + os.getenv('qtjt') + '&pid=0&scene=1089'
headers = {
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2a) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wxf2b0ee8ed60663b4/6/page-frame.html'
}
data = {
    "hid": "30"
}

response = requests.post(url, headers=headers, json=data)
json_data = response.json()

print(json_data)
