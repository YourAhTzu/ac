'''
BY:YourAhTzu
完成日期:1.3 晚上19:55
new Env('金典satine');
一天一次抓access-token的数据填入satine变量
'''
import os
import requests
def sign():
    url = "https://msmarket.msx.digitalyili.com/gateway/api/member/daily/sign"
    headers = {
        "Host": "msmarket.msx.digitalyili.com",
        "Connection": "keep-alive",
        "Content-Length": "2",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002CCA) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "access-token": os.environ.get("satine"),
        "Accept-Encoding": "gzip,compress,br,deflate",
        "tenant-id": "1718857849685876737",
        "scene": "1005",
        "Referer": "https://servicewechat.com/wxf32616183fb4511e/541/page-frame.html",
        "content-type": "application/json"
    }
    data = {}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        sign = result["data"]["dailySign"]
        print(f"签到结果:{sign}")
def point():    
    url = "https://msmarket.msx.digitalyili.com/gateway/api/member/point"
    headers = {
        "Host": "msmarket.msx.digitalyili.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "atv-page": "",
        "source-type": "",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002CCA) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "register-source": "",
        "content-type": "application/json",
        "access-token": os.environ.get("satine"),
        "forward-appid": "",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "tenant-id": "1718857849685876737",
        "scene": "1089",
        "Referer": "https://servicewechat.com/wxf32616183fb4511e/541/page-frame.html"
    }
    response = requests.get(url, headers=headers)
    response_data = response.json()
    data = response_data["data"]
    print(f"当前共有积分:{data}")
sign()
point()