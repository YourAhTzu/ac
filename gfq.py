new Env('共富签');
import requests
import os

auth_str = os.getenv('gfq')
AUTH_LIST = auth_str.split('@')

url = 'https://crm.rabtv.cn/v2/index/signIn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; V2068A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36;xsb_ruian;xsb_ruian;2.31.742;native_app',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://crm.rabtv.cn',
    'X-Requested-With': 'com.test.android.app.ruian',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://crm.rabtv.cn/sign/index.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

for auth in AUTH_LIST:
    headers['Authorization'] = auth
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        code = data['code']
        if code == 0:
            print("签到失败:", data['msg'])
        else:
            score = data['data']['score']
            thumb_url = data['data']['info']['thumb']
            continue_sign_num = data['data']['continue_sign_num']
            print(f"签到成功，得分为{score}，缩略图URL为{thumb_url}，连续签到次数为{continue_sign_num}")
    else:
        print("请求失败，状态码为:", response.status_code)
