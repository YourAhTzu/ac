'''
new Env('天瑞地安——共富签');
变量名：共富签抓Authorization(有些号动态验证签到自己看看)
q群：777974608（不定时开关）
'''
import requests
import os

def qd(auth_list):
    url = 'https://crm.rabtv.cn/v2/index/signIn'
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    for counter, auth in enumerate(auth_list, start=1):
        headers['Authorization'] = auth
        print(f"开始执行第 {counter} 个账号的签到任务")
        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            code = data.get('code')

            if code == 0:
                print(f"账号签到失败:", data.get('msg'))
            else:
                continue_sign_num = data['data']['continue_sign_num']

                if continue_sign_num in [5, 7, 15, 25]:
                    run_code(auth, continue_sign_num)
                    cs(auth, continue_sign_num)

                    # Print the information here if needed
                    score = data['data']['score']
                    thumb_url = data['data']['info']['thumb']
                    print(f"账号签到成功，得分为 {score}，连续签到次数 {continue_sign_num}")

def run_code(auth, continue_sign_num):
    url = 'https://crm.rabtv.cn/v2/user/mineContinueSignCurrentMonth'
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': auth
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            for item in data['data']:
                print('连续签到:', item['text'], '连续奖励id:', item['id'])
                print('---')
                cs(auth, item['id'])

def cs(auth, id):
    url = "https://crm.rabtv.cn/v2/user/getPrizeV"
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': auth
    }
    payload = {"id": id}
    response = requests.post(url, headers=headers, data=payload)
    data = response.json()
    code = data.get("code")
    if code == 0:
        msg = data.get("msg")
        print("返回消息:", msg)
    else:
        score = data["data"]["score"]
        print("得分:", score)

if __name__ == '__main__':
    auth_string = os.getenv('gfq')
    auth_list = auth_string.split('@')

    for auth in auth_list:
        qd([auth])