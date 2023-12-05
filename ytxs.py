''' 
new Env('引体向上');
抓apichuanti.scleader.cn/域名的Authorization要bearer后面数据多号@隔开
年终奖项目
'''
import os
import requests

def notice():
    print("开始获取公告")
    url = "https://ghproxy.smallfawn.top/https://raw.githubusercontent.com/YourAhTzu/ac/main/Notice.json"
    try:
        response = requests.get(url)
        data = response.text
        print(data)
    except requests.RequestException as e:
        print(f"Error occurred while fetching notice: {e}")

def signIn(account_token, index):
    url = "https://apichuanti.scleader.cn/chuanti-mcs/app-api/v1/score/task/get/user/signIn"
    headers = {
        "Authorization": f"bearer {account_token}",
        "Content-Length": "0",
        "Host": "apichuanti.scleader.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/4.9.1"
    }
    try:
        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            if 'message' in response_data:
                message = response_data['message']
                print(f"开始运行第{index+1}个账号, 运行结果: {message}")
        else:
            print(f"账号: {account_token}, 请求失败，状态码: {response.status_code}")

    except requests.RequestException as e:
        print(f"账号: {account_token}, 请求出错: {e}")

def main():
    accounts_env = os.getenv("gfq")
    if accounts_env:
        accounts = accounts_env.split("@")
    else:
        accounts = []
    notice()
    for index, account_token in enumerate(accounts):
        signIn(account_token, index)

if __name__ == "__main__":
    main()