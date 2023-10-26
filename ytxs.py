''' 
new Env('引体向上');
抓任意域名的Authorization要bearer后面数据多号@隔开
年终奖项目
'''
import os
import requests

accounts_env = os.getenv("ytxs")
if accounts_env:
    accounts = accounts_env.split("@")
else:
    accounts = []
for index, account_token in enumerate(accounts):
    headers = {
        "Authorization": f"bearer {account_token}",
        "Content-Length": "0",
        "Host": "apichuanti.scleader.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/4.9.1"
    }

    url = "https://apichuanti.scleader.cn/chuanti-mcs/app-api/v1/score/task/get/user/signIn"
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        if 'message' in response_data:
            message = response_data['message']
            print(f"开始运行第{index+1}个账号, 运行结果: {message}")
    else:
        print(f"账号: {account_token}, 请求失败，状态码: {response.status_code}")