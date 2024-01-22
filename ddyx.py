"""
cron: 0 8 * * *
new Env('点点优选');
微信捉包new.zzpt.top中的userid
青龙变量 export ddyx="userid@userid" 多账号@隔开
只做了抽其他再说
"""
import os
import requests
import time
import random

def sign(token):
    url = "https://new.zzpt.top/mini/jigsaw/get"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "38",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, compress, br, deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }

    data = {
        "messageStatus": "",
        "userToken": "",
        "accessType": "1"
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    msg = response_data["msg"]
    print(msg)

if __name__ == "__main__":
    userids = os.getenv("ddyx") 
    if userids:
        userids_list = userids.split("@") 
        for i in range(8):
            for userid in userids_list:
                sign(userid)
                time.sleep(5 + 5 * random.random())
    else:
        print("未找到环境变量ddyx")
