'''
new Env('江铃智行');
'''
import requests
import os
def signIn(token):
    url = "https://superapp.jmc.com.cn/jmc-zx-app-owner/v1/signIn/add"
    headers = {
        "Host": "superapp.jmc.com.cn",
        "Content-Length": "33",
        "Access-Token": token,
        "Content-Type": "application/json"
    }
    data = {
        "activityCode": "HD202401010007"
    }
    response = requests.post(url, headers=headers, json=data)
    json_data = response.json()
    msg = json_data["resultMsg"]
    print(f"签到结果:{msg}")
if __name__ == "__main__":
    tokens = os.environ.get('jlzx') 
    if not tokens:
        print("获取账号失败，检查是否配置正确")
    else:
        tokens_list = tokens.split('@')
        num = len(tokens_list)
        for num, token in enumerate(tokens_list, start=1):
            print(f"=====开始执行第{num}个账号任务=====")
            signIn(token)
            print("==============================")