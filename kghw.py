import os
import requests

class AC:
    def __init__(self, appid, openid, refresh_token):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.122 Mobile Safari/537.36 XWEB/1260059 MMWEBSDK/20240501 MMWEBID/2307 MicroMessenger/8.0.50.2701(0x28003252) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
            'Content-Type': "application/json"
        }
        self.data = {
            "appid": appid,
            "openid": openid,
            "refresh_token": refresh_token
        }
    
    def login(self):
        url = "https://www.kugua.com/wxapp/refreshToken"
        response = requests.post(url, headers=self.headers, json=self.data)
        data = response.json()
        if data['status'] == "0000":
            token = data["data"]["token"]
            print(f"最新token为：{token}")
            return token
        else:
            codemsg = data["codemsg"]
            print(f"{codemsg}")
            return None
    
    def withdrawal(self, token, withdrawal_id):
        url = "https://www.kugua.com/wxapp/withdrawal/withdrawal"
        data = {
            "token": token,
            "withdrawalId": withdrawal_id,
            "appid": self.data["appid"],
            "openid": self.data["openid"]
        }
        response = requests.post(url, headers=self.headers, json=data)
        data = response.json()
        if data['status'] == "0000":
            codemsg = data["codemsg"]
            print(f"提现结果为{codemsg}")
        else:
            codemsg = data["codemsg"]
            print(f"{codemsg}")
    
    def main(self):
        token = self.login()
        if token:
            withdrawal_id = 8  # 提现ID
            self.withdrawal(token, withdrawal_id)

if __name__ == '__main__':
    kghw = os.environ.get('kghw')
    if not kghw:
        print("请设置环境变量 'kghw' 后再运行")
    else:
        kghw_list = kghw.split('@')
        for num, kghw_item in enumerate(kghw_list, start=1):
            appid, openid, refreshToken = kghw_item.split('&')
            print(f"=====开始执行第{num}个账号任务=====")
            ac = AC(appid, openid, refreshToken)
            ac.main()
