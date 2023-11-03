'''
抓token邀请入口在群（盘子性质目前拉一个人5毛需要找客服激活）
new Env('聚宝抽屉');
'''
import os
import requests
import time

print("开始执行签到任务")
url = "https://233.yyyy.run/api/sign/userSignIn"
headers = {
    "Host": "233.yyyy.run",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "appid": "wxfa4fc719bda479aa",
    "content-type": "application/x-www-form-urlencoded",
    "os": "ios",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2f) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wxfa4fc719bda479aa/6/page-frame.html"
}

tokens = os.getenv("jbct").split("@") 
for _ in range(3):  # This loop will run three times
    for token in tokens:
        headers["token"] = token
        print("延迟十分钟")
        time.sleep(600)

        response = requests.post(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            msg = data.get("msg")
            print("签到结果：", msg)
