'''
太久没更新了随机更新一个年终奖吧物品少看情况挂
抓任意URL的userHash只要Bearer后面的数据即可
new Env('IT之家');'''
import requests
import os
class ITZJ():
    def __init__(self, token):
        self.token = token
    def sign(self):
        url = f"https://napi.ithome.com/api/UserSign/WeChatSign?userHash=Bearer {self.token}&coinHistoryType=157"#此处为请求的URL
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260213 MMWEBSDK/20240802 MMWEBID/2307 MicroMessenger/8.0.53.2740(0x2800353E) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 miniProgram/wx8869812e2ddf7133",
            'sec-ch-ua-platform': "\"Android\""
        }
        response = requests.get(url, headers=headers)
        print(response.text)
if __name__ == "__main__":
    tokens = os.environ.get('itzj')
    if not tokens:
        print("请设置变量名"itzj")
    else:
        tokens_list = tokens.split('@')
        for index, token in enumerate(tokens_list, start=1):
            print(f"=====开始执行第{index}个账号任务=====")
            it = ITZJ(token)
            it.sign()        