"""
@Qim出品 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
植白说官方商城_V1.2  签到 牛奶活动
抓https://www.kozbs.com/demo/取出X-Dts-Token
export zbstoken=X-Dts-Token
多账号用'===='隔开 例 账号1====账号2
corn：0 0 8 * * ?
加了一个PushPlus推送
new Env('植白说');
"""
import os
import requests

# 读取 PushPlus Token
pushplus_token = os.environ.get('PUSHPLUS_TOKEN', '')
print("PushPlus Token:", pushplus_token)

if not pushplus_token:
    print("请配置PushPlus Token！")
    exit(1)

accounts = os.getenv('zbstoken')
response = requests.get('https://gitee.com/shallow-a/qim9898/raw/master/label.txt').text
print(response)

if accounts is None:
    print('你没有填入zbstoken，咋运行？')
else:
    accounts_list = os.environ.get('zbstoken').split('====')
    num_of_accounts = len(accounts_list)
    print(f"获取到 {num_of_accounts} 个账号")

    result_list = []  # 存储所有账号的签到和分享结果以及积分余额

    # 遍历所有账号进行签到和分享任务
    for i, account in enumerate(accounts_list, start=1):
        values = account.split('@')
        zbstoken = values[0]
        print(f"\n=======开始执行账号{i}=======")
        url = 'https://www.kozbs.com/demo/wx/home/signDay'
        headers = {
            'X-DTS-Token': zbstoken,
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.39 (0x18002733) NetType/WIFI Language/zh_CN',
        }
        response = requests.get(url, headers=headers)
        response.code = response.json()
        if response.code['errno'] == 0:
            signCount = response.code['data']['signCount']
            integral = response.code['data']['integral']
            print(f"签到成功----{signCount}\n积分余额----{integral}")

            # 添加当前账号的签到结果和积分余额到列表中
            result_list.append(f"账号{i}：签到成功--{signCount}，积分余额--{integral}")
        else:
            print('请求失败')

        # 分享任务
        for j in range(3):
            url = 'https://www.kozbs.com/demo/wx/user/addIntegralByShare'
            response = requests.get(url, headers=headers)
            response.code = response.json()
            if response.code['errno'] == 0:
                print(f"第{j + 1}分享---成功")
                # 添加当前账号的分享结果到列表中
                result_list.append(f"账号{i}：分享{j + 1}成功")
            else:
                print('请求失败')

    # 将所有账号的签到、分享结果和积分余额的字符串以换行符连接成一个大字符串
    result_str = '\n'.join(result_list)

    # 构造推送的请求参数
    push_url = 'http://www.pushplus.plus/send'
    push_data = {
        'token': pushplus_token,
        'title': f"推送结果({num_of_accounts}个账号)",
        'content': result_str,
    }

    # 发送推送请求
    push_response = requests.post(push_url, data=push_data)
    push_result = push_response.json()
    if push_result['code'] == 200:
        print("推送成功")
    else:
        print("推送失败")
