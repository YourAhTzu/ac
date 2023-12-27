'''
new Env('青柳同城圈');
合并领取红包和部分积分任务
'''
import requests
import json
import random
import time
import os

def red(token):
    print(">>>>>开始领取红包<<<<<")
    url = 'https://tc.qzfwckj.com/api/red/index'
    headers = {
            'charset': 'utf-8',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C3F) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android',
            'content-type': 'application/json',
            'Accept-Encoding': 'gzip,compress,br,deflate',
            'accept': 'application/json, text/plain, */*',
            'token': token,
            'Referer': 'https://servicewechat.com/wx9886f1558114d887/7/page-frame.html'
    }
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response_data["code"] == 1:
        data = response_data["data"]
        for item in data:
            id = item["id"]
            openRed(token, id)
            delay()
def openRed(token, id):
    url = 'https://tc.qzfwckj.com/api/red/openRed'
    params = {
        'id': id 
    }
    headers = {
            'charset': 'utf-8',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C3F) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android',
            'content-type': 'application/json',
            'Accept-Encoding': 'gzip,compress,br,deflate',
            'accept': 'application/json, text/plain, */*',
            'token': token,
            'Referer': 'https://servicewechat.com/wx9886f1558114d887/7/page-frame.html'
    }
    response = requests.get(url, params=params, headers=headers)
    response_data = response.json()
    if response_data["code"] == 1:
        data = response_data["data"]
        print("恭喜获得:", data)
        delay()
def addSigninRecord(token):
    print(">>>>>执行签到<<<<<")
    url = "https://tc.qzfwckj.com/api/mall/addSigninRecord"
    headers = {
        "Host": "tc.qzfwckj.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C3F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "accept": "application/json, text/plain, */*",
        "token": token,
        "Referer": "https://servicewechat.com/wx9886f1558114d887/8/page-frame.html"
    }
    response = requests.post(url, headers=headers)
    result = response.json()
    msg = result["msg"]
    print(f"签到结果: {msg}")
    delay()
def index(token):
    print(">>>>>执行评论和点赞<<<<<")
    url = "https://tc.qzfwckj.com/api/circle/index"
    headers = {
        "Host": "tc.qzfwckj.com",
        "Connection": "keep-alive",
        "Content-Length": "47",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C3F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip, compress, br, deflate",
        "accept": "application/json, text/plain, */*",
        "token": token,
        "Referer": "https://servicewechat.com/wx9886f1558114d887/8/page-frame.html"
    }
    data = {
        "page": 1,
        "limit": 10,
        "content": "",
        "category": 0
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        list_data = result["data"]["list"]
        for item in list_data:
            circle_id = item["id"]
            comment(token, circle_id)
            like(token, circle_id)
            delay()
def comment(token, circle_center_id):
    url = "https://tc.qzfwckj.com/api/circle/comment"
    headers = {
        "Host": "tc.qzfwckj.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C3F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "accept": "application/json, text/plain, */*",
        "token": token,
        "Referer": "https://servicewechat.com/wx9886f1558114d887/8/page-frame.html"
    }
    data = {
        "circle_center_id": circle_center_id,
        "content": "漂亮"
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    msg = result["msg"]
    print(f"评论结果: {msg}")
def like(token, circle_center_id):
    url = "https://tc.qzfwckj.com/api/circle/like"
    headers = {
        "Host": "tc.qzfwckj.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C3F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "accept": "application/json, text/plain, */*",
        "token": token,
        "Referer": "https://servicewechat.com/wx9886f1558114d887/8/page-frame.html"
    }
    data = {
        "id": circle_center_id,
        "like": "true"
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    msg = result["msg"]
    print(f"点赞结果: {msg}")
def delay():
    delay_time = random.randint(1, 15)
    print(f"等待{delay_time}秒")
    time.sleep(delay_time)
def main():
    token = os.getenv('qltcq')
    if token:
        print("----------------开始执行任务---------------")
        red(token)
        addSigninRecord(token)
        index(token)
    else:
        print("请设置数据")
if __name__ == "__main__":
    main()