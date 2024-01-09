'''
new Env('梦幻岛屿');
BY:YourAhTzu
日期:1.10 7:53 (修复多号报错)
注册链接:http://mh.youwanzz.com/#/pages/reg?id=a413
格式:账号&密码
去主页绑定zfb在运行脚本需要签到十天
'''
import os
import requests
import json
import random
import time
def login(tel, pwd):
    print(">>>>>开始登录账号<<<<<")
    url = "http://mhapi.youwanzz.com:4005/index/Login"
    headers = {
        "Host": "mhapi.youwanzz.com:4005",
        "Connection": "keep-alive",
        "Content-Length": "45",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36",
        "custom-header": "hello",
        "content-type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "http://mh.youwanzz.com",
        "X-Requested-With": "mark.via",
        "Referer": "http://mh.youwanzz.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
        "txyzm": "",
        "type": "dl",
        "tel": tel,
        "pwd": pwd
    }
    response = requests.post(url, headers=headers, data=data)
    data = response.json()
    if "token" in data:
        token = data["token"]
        uid = data["id"]
        print(data["msg"])
        return token, uid
    else:
        print("登录失败:", data["msg"])
        return None, None

def qian_dao(token, uid):
    print(">>>>>开始执行签到<<<<<")
    url = "http://mhapi.youwanzz.com:4005/Index/QianDao"
    headers = {
        "Host": "mhapi.youwanzz.com:4005",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36",
        "custom-header": "hello",
        "content-type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "http://mh.youwanzz.com",
        "X-Requested-With": "mark.via",
        "Referer": "http://mh.youwanzz.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
        'id': uid,
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    print(result['msg'])

def LingRenWu(token, uid):
    print(">>>>>开始领取月卡金币<<<<<")
    url = "http://mhapi.youwanzz.com:4005/My/LingRenWu"
    headers = {
        "Host": "mhapi.youwanzz.com:4005",
        "Connection": "keep-alive",
        "Content-Length": "52",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36",
        "custom-header": "hello",
        "content-type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "http://mh.youwanzz.com",
        "X-Requested-With": "mark.via",
        "Referer": "http://mh.youwanzz.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
        'id': uid,
        'token': token,
        "kid": "1"
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    print(result['msg'])

def GetHome(token, uid):
    print(">>>>>开始获取红包和金币<<<<<")
    url = 'http://mhapi.youwanzz.com:4005/Index/GetHome'
    headers = {
        'Host': 'mhapi.youwanzz.com:4005',
        'Connection': 'keep-alive',
        'Content-Length': '46',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36',
        'custom-header': 'hello',
        'content-type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'http://mh.youwanzz.com',
        'X-Requested-With': 'mark.via',
        'Referer': 'http://mh.youwanzz.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {
        'id': uid,
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.text
    data = json.loads(response_data)
    jinbi = data["jinbi"]
    hongbao = data["hongbao"]
    print("当前金币:", jinbi,"当前红包:", hongbao)

if __name__ == '__main__':
    mhdy = os.environ.get('mhdy')
    if mhdy:
        account_list = mhdy.split('@')
        for account in account_list:
            tel, pwd = account.split('&')
            token, uid = login(tel, pwd)
            
            if token is not None and uid is not None:
                login_delay = random.randint(15, 25)
                time.sleep(login_delay)
                qian_dao(token, uid)
                LingRenWu(token, uid)
                GetHome(token, uid)
                task_delay = random.randint(5, 10)
                print(f"等待{task_delay}秒后执行下一个任务")
                time.sleep(task_delay)

                print("-------------------------------------")
            else:
                print("账号登录失败，请检查账号密码是否正确")
                print("-------------------------------------")
    else:
        print("请设置环境变量 mhdy")