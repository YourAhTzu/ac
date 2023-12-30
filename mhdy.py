'''
new Env('梦幻岛屿');
BY:YourAhTzu
日期:12.30 22:51
注册链接:http://mh.youwanzz.com/#/pages/reg?id=a413
格式:账号&密码
去主页绑定zfb在运行脚本需要签到十天
'''
import os
import requests
def login(tel, pwd):
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
    return token, uid
def qian_dao(token, uid):
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
if __name__ == '__main__':
    mhdy = os.environ.get('mhdy')
    if mhdy:
        tel, pwd = mhd.split('&')
        token, uid = login(tel, pwd)
        qian_dao(token, uid)
    else:
        print("请设置环境变量mhdy")