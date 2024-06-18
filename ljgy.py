'''
new Env('丽瑾国韵');
账号&密码 多账号换行或者@分隔
'''
import requests
import os
from os import path
import sys
headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220099 MMWEBSDK/20240404 MMWEBID/2307 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
    'Accept': "application/json, text/plain, */*",
    'sec-ch-ua': "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Android WebView\";v=\"122\"",
}
def login(username, password):
    url = "https://wep.qzlcis.com/api/index/login"
    data = {
        "username": username,
        "password": password,
        "token": None
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    if json_data.get("code") == 1:
        token = json_data["data"]["token"]
        info = json_data["info"]
        print(f"登录成功: {info}")
        return token
    else:
        print(f"登录失败: {json_data.get('info')}")
        return None
def sign(token):
    url = "https://wep.qzlcis.com/api/user/sign"
    data = {"token": token}
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    code = json_data.get("code")
    info = json_data.get("info")
    if code == 1:
        reward_num = json_data["data"].get("reward_num", "未知")
        print(f"签到成功: {info}, 奖励数量: {reward_num}")
    else:
        print(f"签到失败: {info}")
def info(token):
    url = "https://wep.qzlcis.com/api/user/info"
    data = {"token": token}
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    code = json_data.get("code")
    info = json_data.get("info")
    if code == 1:
        mobile = json_data["data"]["mobile"]
        money = json_data["data"]["money"]
        print(f"账户{mobile}余额为{money}")
    else:
        print(f"获取账户信息失败: {info}")
if __name__ == "__main__":
    ljgy = os.environ.get('ljgy')
    if not ljgy:
        print("请设置环境变量在运行")
    else:
        ljgy_list = ljgy.split('@')
        for num, ljgy_item in enumerate(ljgy_list, start=1):
            username, password = ljgy_item.split('&')
            print(f"=====开始执行第{num}个账号任务=====")
            print("---------开始执行账号登录")
            token = login(username, password)
            if token:
                print("---------开始执行签到任务---------")
                sign(token)
                print("---------开始执行获取账户信息任务---------")
                info(token)