'''
new Env('东方棘市');
东方棘市每日签到,分享提现后续完成可关注github
抓token变量dfjs多号@ 
7.1号19:38更新自动提现(PS余额不满足1则不进行提现)
'''
import requests
import os
def sign(token):
    url = "https://ys.shajixueyuan.com/api/user_sign/sign"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220099 MMWEBSDK/20240404 MMWEBID/2307 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        'token': token
    }
    response = requests.post(url, headers=headers)
    data = response.json()
    if data['code'] == 1:
        msg = data['data']['msg']
        m_sg = ["msg"]
        energy_release = data["data"]["rewards_info"]["energy_release"]
        print(f"签到结果:{m_sg},释放{energy_release}能量果子,获得了{msg}")
    else:
        msg = data["msg"]
        print(f"签到失败原因:{msg}")
def issueRewards(token):
    url = "https://ys.shajixueyuan.com/api/quest.quest/issueRewards"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220099 MMWEBSDK/20240404 MMWEBID/2307 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        'token': token
    }
    data = {
          "quest_id": 4
    }
    response = requests.post(url, json=data,headers=headers)
    data = response.json()
    msg = data['msg']
    print(f"分享结果:{msg}")
def info(token):
    url = "https://ys.shajixueyuan.com/api/user/info"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220099 MMWEBSDK/20240404 MMWEBID/2307 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        'token': token
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if data['code'] == 1:
        accumulated_fruits = float(data["data"]["accumulated_fruits"])  
        nickname = data["data"]["nickname"]
        print(f"用户:{nickname} 当前余额:{accumulated_fruits}")
        if accumulated_fruits >= 1:
            apply(token)  
        else:
            print("余额不足，无法进行提现")
    else:
        msg = data["msg"]
        print(f"查询失败→{msg}")
def apply(token):
    url = "https://ys.shajixueyuan.com/api/user.user_withdraw/apply"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220099 MMWEBSDK/20240404 MMWEBID/2307 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        'token': token
    }
    data = {
        "fruit_withdraw_amount": "1",
        "pay_gateway": "wechat"
    }
    response = requests.post(url, json=data, headers=headers)
    data = response.json()
    msg = data['msg']
    print("提现结果:", msg)
if __name__ == "__main__":
    tokens = os.environ.get('dfjs') 
    if not tokens:
        print("获取账号失败，请检查配置是否正确")
    else:
        tokens_list = tokens.split('@')
        for index, token in enumerate(tokens_list, start=1):
            print(f"=====开始执行第{index}个账号任务=====")
            print(f"=====开始执行签到任务=====")
            sign(token)
            print(f"=====开始执行分享任务=====")
            issueRewards(token)
            print(f"=====开始执行查询和提现任务=====")
            info(token)
            print("==============================")