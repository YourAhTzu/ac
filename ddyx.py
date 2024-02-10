"""
cron: 0 8 * * *
new Env('点点优选');
微信捉包new.zzpt.top中的userid
青龙变量 export ddyx="userid@userid" 多账号@隔开  58行改助力码进行账号助力默认助力作者 (更新频繁)
"""
import os
import requests
import time
import random
def info(token):
    url = "https://new.zzpt.top/mini/user/userInfo"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160055 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/6/page-frame.html"
    }
    response = requests.post(url, headers=headers)
    data = response.json()
    userName = data["data"]["userName"]
    userToken = data["data"]["userToken"]
    totalPrice = data["data"]["totalPrice"]
    newYearPrice = data["data"]["newYearPrice"]
    dragonGold = data["data"]["dragonGold"]
    print(f"用户:{userName}")
    print(f"助力码:{userToken}")
    print(f"钱包:{totalPrice}")
    print(f"龙卡:{newYearPrice}")
    print(f"龙币:{dragonGold}")
def sign(token):
    url = "https://new.zzpt.top/mini/task/free"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }
    response = requests.post(url, headers=headers)
    response_data = response.json()
    code = response_data["code"]
    if code == 0:
        msg = response_data["msg"]
        print(f"签到结果:{msg}")
    else:
        print("已签到")     
def video(token):
    url = "https://new.zzpt.top/mini/task/video"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }
    response = requests.post(url, headers=headers)
    response_data = response.json()
    code = response_data["code"]
    if code == 0:
        msg = response_data["msg"]
        print(f"观看结果:{msg}")
    else:
        print("已完成")
def jigsaw(token):
    url = "https://new.zzpt.top/mini/jigsaw/get"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "38",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F35) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, compress, br, deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/7/page-frame.html"
    }
    data = {
        "messageStatus": "",
        "userToken": "",
        "accessType": "1"
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    if result.get("code") != 0:
        msg = result.get("msg")
        print(f"抽奖结果: {msg}")
        return
    else:
        print("当前任务已完成执行跳过")
def exchange(token):
    url = "https://new.zzpt.top/mini/jigsaw/exchange"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    if result.get("code") != 0:
        msg = result.get("msg")
        print(f"兑换结果: {msg}")
        return
    else:
        print("当前任务已完成执行跳过")

def Exchange(token):
    url = "https://new.zzpt.top/mini/jigsaw/exchangePriceByCard/87"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    if result.get("code") != 0:
        msg = result.get("msg")
        print(f"兑换结果: {msg}")
        return
    else:
        print("当前任务已完成执行跳过")
if __name__ == "__main__":
    userid = os.environ.get("ddyx")
    if userid:
        tokens_list = userid.split("@")
        for i, token in enumerate(tokens_list):
            print(f">>>>>开始执行第{i+1}个账号任务<<<<<")  
            print(">>>>>领取抽奖机会<<<<<")
            sign(token)
            print(">>>>>开始观看广告<<<<<")    
            for _ in range(2):
                video(token)
                time.sleep(random.randint(15, 30))
            print(">>>>>开始执行抽奖<<<<<")
            for _ in range(4):
                lottery(token)
                time.sleep(random.randint(1, 10))
            print(">>>>>福利红包<<<<<")
            exchange(token)
            print(">>>>>龙卡兑换余额<<<<<")
            Exchange(token)
            print(">>>>>用户查询<<<<<")
            info(token)
            print("========================================")  
    else:
        print("未找到环境变量ddyx")
