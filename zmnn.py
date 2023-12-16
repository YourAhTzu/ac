"""
new Env('战马能量小程序');
抓头部safe填入zmnn(简单几个任务有能力自己加)
"""
import os
import requests
safe = os.getenv('zmnn')  # 自定义变量名字
def message():
    url = f"https://zm.t7a.cn/api/getusercenter.php?safe={safe}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110039 MMWEBSDK/20231002 MMWEBID/2307 MicroMessenger/8.0.43.2480(0x28002B51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Referer": "https://servicewechat.com/wx94dca6ef07a54c55/143/page-frame.html",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        nickname = data["nickname"]
        nowscore = data["nowscore"]

        print("用户:", nickname, "当前积分:", nowscore)
    else:
        print("请求失败，状态码:", response.status_code)

def signin():
    print("开始执行签到任务")
    url = f'https://zm.t7a.cn/api/checkin.php?safe={safe}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110039 MMWEBSDK/20231002 MMWEBID/2307 MicroMessenger/8.0.43.2480(0x28002B51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'Referer': 'https://servicewechat.com/wx94dca6ef07a54c55/143/page-frame.html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, compress, br, deflate'
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()
    msg = response_json['msg']
    print("签到结果:", msg)

def strokehorse():
    print("开始执行抚摸任务")
    url = f'https://zm.t7a.cn/api/strokehorse.php?safe={safe}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110039 MMWEBSDK/20231002 MMWEBID/2307 MicroMessenger/8.0.43.2480(0x28002B51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'Referer': 'https://servicewechat.com/wx94dca6ef07a54c55/143/page-frame.html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, compress, br, deflate'
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()
    msg = response_json['msg']
    print("签到结果:", msg)

def checkslgift():
    print("开始执行分享任务")
    url = f'https://zm.t7a.cn/api/checkslgift.php?safe={safe}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110039 MMWEBSDK/20231002 MMWEBID/2307 MicroMessenger/8.0.43.2480(0x28002B51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'Referer': 'https://servicewechat.com/wx94dca6ef07a54c55/143/page-frame.html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, compress, br, deflate'
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()
    msg = response_json['msg']
    print("喂马结果:", msg)

def horseeat():
    print("开始执行喂马任务")
    url = f'https://zm.t7a.cn/api/horseeat.php?safe={safe}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110039 MMWEBSDK/20231002 MMWEBID/2307 MicroMessenger/8.0.43.2480(0x28002B51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'Referer': 'https://servicewechat.com/wx94dca6ef07a54c55/143/page-frame.html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, compress, br, deflate'
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()
    msg = response_json['msg']
    print("喂马结果:", msg)

if __name__ == "__main__":
    signin()
    strokehorse()
    checkslgift()
    horseeat()