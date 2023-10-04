''' 
@阿慈
垃圾毛自己玩吧
农好优下载链接麻烦走个头http://wap.nonghaoyou.cn/Public/reg/recom/271866
new Env('农好优'); 
'''
import requests
import time
import random
import os


url = "http://wap.nonghaoyou.cn/Member/ad_video_api"

headers = {
    "Host": "wap.nonghaoyou.cn",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; V2068A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/104",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://wap.nonghaoyou.cn",
    "Referer": "http://wap.nonghaoyou.cn/Member/signin?xapp-target=blank",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

cookie = os.environ.get("nhy")  
if cookie:
    headers["Cookie"] = cookie
else:
    print("未知bug停止运行")
    exit()

data = {
    "uid": "11984"
}

def sign_in():
    response = requests.post(url, headers=headers, data=data)
    json_data = response.json()
    if json_data.get("status") == 1:
        print("恭喜骚年签到成功")

def main():
    for i in range(1, 11):
        sign_in()
        
        delay = random.randint(30, 60)  
        print(f"骚等 {delay} 秒")
        time.sleep(delay)

    print("签到完成")

if __name__ == "__main__":
    main()
