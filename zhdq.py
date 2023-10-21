''' 
抓Authorization记得删除Bearer填变量zhdq多号@隔开（什么时候签的到怎么定时）链接http://www.mofamoli.com/h5/reg.html?invite_code=JYWG5E
new Env('智慧地球');
'''
import os
import requests
import datetime

accounts = os.environ.get("zhdq").split("@")
url = "http://www.zhihuidiqiu.com.cn/api/v2/mining/start"
headers = {
    "os": "android",
    "appVersionCode": "3",
    "appVersionName": "1.0.2",
    "Accept": "application/json",
    "Local": "1",
    "Content-Length": "0",
    "Host": "www.zhihuidiqiu.com.cn",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.10.0"
}

def sign_in(account):
    auth = f"Bearer {account.strip()}"
    headers["Authorization"] = auth

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

    headers["datetime"] = formatted_time

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print("签到成功")
    else:
        print("正在收益中")

def main():
    for index, account in enumerate(accounts):
        print(f"执行第{index+1}账号任务")
        sign_in(account)

if __name__ == "__main__":
    main()