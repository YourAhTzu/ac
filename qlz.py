'''
@阿慈 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
corn：10 10 * * 
new Env('巧乐兹'); 
仅签到，环境变量名字qlz
'''
import os
import requests

url = "https://kapi.yili.com/qlz/api/user/daily/sign?exParams=false"
accessToken = os.getenv("qlz")
headers = {
    "Host": "kapi.yili.com",
    "Connection": "keep-alive",
    "accessToken": accessToken,
    "content-type": "application/x-www-form-urlencoded",
    "scene": "1089",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x1800292e) NetType/4G Language/zh_CN",
}

print("开始执行签到")

response = requests.get(url, headers=headers)
data = response.json()

if "bonusPoints" in data:
    print("获得奖励积分数:", data["bonusPoints"])
else:
    print("已签到")
