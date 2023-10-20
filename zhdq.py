#抓Authorization填变量zhdq多号@隔开（什么时候签的到怎么定时）链接http://www.mofamoli.com/h5/reg.html?invite_code=JYWG5E
import os
import requests

accounts = os.environ.get("zhdq").split("@")
url = "http://www.zhihuidiqiu.com.cn/api/v2/mining/start"
headers = {
    "os": "android",
    "appVersionCode": "3",
    "appVersionName": "1.0.2",
    "datetime": "2023-10-20 18:28:13.700",
    "Accept": "application/json",
    "Local": "1",
    "Content-Length": "0",
    "Host": "www.zhihuidiqiu.com.cn",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.10.0"
}

for account in accounts:
    auth = f"Bearer {account.strip()}"
    headers["Authorization"] = auth
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print("签到成功")
    else:
        print("正在收益中")
