'''
new Env('梦幻岛屿');
BY:YourAhTzu
日期:12.31 04:50
注册链接:http://mh.youwanzz.com/#/pages/reg?id=a413
格式:账号&密码
去主页绑定zfb在运行脚本需要签到十天
'''
import os
import requests
import json

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
    token = data["token"]
    uid = data["id"]
    print(data["msg"])
    return token, uid

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
    return jinbi
def DuiHuanKj(token, uid):
    url = 'http://mhapi.youwanzz.com:4005/My/DuiHuanKj'
    headers = {
        'Host': 'mhapi.youwanzz.com:4005',
        'Connection': 'keep-alive',
        'Content-Length': '52',
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
        'token': token,
        'kid': '1'
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.text
    data_dict = json.loads(response_data)
    msg = data_dict["msg"]
    print(msg)
if __name__ == '__main__':
    mhdy = os.environ.get('mhdy')
    if mhdy:
        tel, pwd = mhdy.split('&')
        token, uid = login(tel, pwd)
        if token and uid:
            qian_dao(token, uid)
            jinbi = GetHome(token, uid)
            if float(jinbi) > 100:  
                DuiHuanKj(token, uid)
            else:
                print("当前金币不足，无法购买月卡")
    else:
        print("请设置环境变量mhdy")