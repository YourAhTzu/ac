'''
@阿慈 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
corn：10 10 * * 
state有效期非常短一天一抓
更新进群任务
'''
import os
import time
import requests

def sign():
    state = os.environ.get('box57')
    if not state:
        raise ValueError('请设置环境变量 "box57" 的值')

    url = f'https://www.57box.cn/app/index.php?i=2&t=0&v=1&from=wxapp&c=entry&a=wxapp&do=uptaskinfo&state={state}&sign=17e0a5a3ac93839899c742555ee588b0'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x1800292e) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx0288d58351670e0d/79/page-frame.html'
    }
    data = {
        'm': 'greatriver_lottery_operation',
        'id': '35'
    }

    for _ in range(3):
        response = requests.post(url, headers=headers, data=data)
        json_data = response.json()

        message = json_data.get("message", "")
        if json_data.get("errno") == 103:
            print(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] 执行结果:{message}')
        else:
            print(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] 执行结果:{message}')
        time.sleep(5)

def answer():
    state = os.environ.get('box57')
    if not state:
        raise ValueError('请设置环境变量 "box57" 的值')

    url = f'https://www.57box.cn/app/index.php?i=2&t=0&v=1&from=wxapp&c=entry&a=wxapp&do=uptaskinfo&&state={state}&sign=17e0a5a3ac93839899c742555ee588b0'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x1800292e) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx0288d58351670e0d/79/page-frame.html'
    }
    data = {
        'm': 'greatriver_lottery_operation',
        'id': '30',
        'answer': '普通物品不可分解'
    }

    response = requests.post(url, headers=headers, data=data)
    json_data = response.json()

    message = json_data.get("message", "")
    if json_data.get("errno") == 999:
        return {"message": message}
    else:
        return {"message": "答题成功"}


def Into():
    url = 'https://www.57box.cn/app/index.php?i=2&t=0&v=1&from=wxapp&c=entry&a=wxapp&do=uptaskinfo&&state={state}&sign=5d22d319bf2923a29bc4789b17605dce'
    data = {
        'm': 'greatriver_lottery_operation',
        'id': '26',
        'answer': '228899'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x1800292e) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx0288d58351670e0d/79/page-frame.html'
    }

    response = requests.post(url, data=data, headers=headers)
    json_data = response.json()

    if json_data['errno'] == 0:
        print('任务完成')
        
    else:
        print('任务已完成')

if __name__ == '__main__':
    print("开始执行视频")
    sign()
    print("开始执行答题")
    result = answer()
    print(result['message'])
    print("开始执行进群任务")
    Into()
