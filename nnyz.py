'''
new Env('能源宇宙');
变量nnyz格式账号&密码没有多号只有单号
邀请码赏个头（玩法看群里）https://nyshare.igmdns.com/index.html?inviteCode=14605
'''
import requests
import time
import random
import os

def login():
    url = "https://nyapi.igmdns.com/api/login"
    mobile = os.environ.get("nnyz").split("&")[0]
    password = os.environ.get("nnyz").split("&")[1]
    payload = {
        "mobile": mobile,
        "password": password
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; V2068A Build/RP1A.200720.012)"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        token = data.get("data", {}).get("token")
        nickname = data.get("data", {}).get("nickname")
        if token and nickname:
            print(f"登录成功！用户:{nickname}")
            return token
        else:
            print("登录失败,检查账密是否正确")

def ad(token):
    url = 'https://nyapi.igmdns.com/api/ad'
    headers = {
        'Accept-Encoding': 'identity',
        'Content-Type': 'application/json',
        'authorization': token,
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; V2068A Build/RP1A.200720.012)',
        'Host': 'nyapi.igmdns.com',
        'Connection': 'Keep-Alive',
    }
    response = requests.post(url, headers=headers, data='{}')
    print("观看成功")
    delay = random.randint(15, 25)
    time.sleep(delay)

def reward(token):
    url = "http://nyapi.igmdns.com/api/machine/give/reward"
    headers = {
        "Accept-Encoding": "identity",
        "Content-Type": "application/json",
        "authorization": token,
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; V2068A Build/RP1A.200720.012)",
        "Host": "nyapi.igmdns.com",
        "Connection": "Keep-Alive"
    }
    data = {}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        reward_data = response.json()
        reward_spar = reward_data["data"]["rewardSpar"]
        print("获得奖励:", reward_spar, "晶石")
    else:
        print("您已领取今日能源晶石奖励")

token = login()
for _ in range(6):
    ad(token)
reward(token)