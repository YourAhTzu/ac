import requests
import datetime
import os

def Refresh(refreshToken):
    url = "https://cmallapi.haday.cn/buyer-api/passport/token"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.187 Mobile Safari/537.36 XWEB/1260075 MMWEBSDK/20240501 MMWEBID/2307 MicroMessenger/8.0.50.2701(0x28003255) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        'Content-Type': "application/x-www-form-urlencoded",
        'uuid': uuid,
        'charset': "utf-8",
        'Referer': "https://servicewechat.com/wx7a890ea13f50d7b6/612/page-frame.html"
    }
    data = {
        "refresh_token": refreshToken
    }
    response = requests.post(url, data=data, headers=headers)
    data = response.json()
    accessToken = data['accessToken']
    return accessToken 
def sign(accessToken):
    url = "https://cmallapi.haday.cn/buyer-api/sign/activity/sign"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.187 Mobile Safari/537.36 XWEB/1260075 MMWEBSDK/20240501 MMWEBID/2307 MicroMessenger/8.0.50.2701(0x28003255) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        'Content-Type': "application/json",
        'uuid': uuid,
        'envVersion': "release",
        'Authorization': accessToken,
        'charset': "utf-8",
        'Referer': "https://servicewechat.com/wx7a890ea13f50d7b6/612/page-frame.html"
    }
    data = {
        "activity_code": datetime.datetime.now().strftime('%Y%m'),
        "fill_date": ""
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("签到成功")
    else:
        print("已签到过无需再签到")

if __name__ == "__main__":
    htmwg = os.environ.get('htmwg')
    if not htmwg:
        print("请设置环境变量 'htmwg' 后再运行")
    else:
        htmwg_list = htmwg.split('@')
        for num, htmwg_item in enumerate(htmwg_list, start=1):
            uuid, refreshToken = htmwg_item.split('&')
            print(f"=====开始执行第{num}个账号任务=====")
            accessToken = Refresh(refreshToken)  
            if accessToken:
                print(f"获取刷新后的AccessToken:{accessToken}")
                result = sign(accessToken)