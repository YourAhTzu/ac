'''
@阿慈 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
此接口调用小白API
更新环境变量提交PushPlus数据环境名字tz
new Env('线报');
'''
import os
import json
import requests

def send_pushplus_notification(token, title, content, receivers):
    # 构建请求体
    data = {
        'token': token,
        'title': title,
        'content': content,
        'template': 'html',
        'channel': 'wechat',
        'receiver': ','.join(receivers)
    }

    # 发送请求
    response = requests.post('http://www.pushplus.plus/send', json=data)

    # 返回结果
    return response.json()

url = "https://xiaobai.klizi.cn/API/other/xb.php"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Mobile/15E148 Safari/604.1',
    'Accept-Encoding': 'gzip, deflate, br'
}

try:
    with requests.get(url, headers=headers) as response:
        response.raise_for_status()  # 检查响应是否成功
        data = response.json()["data"]
        time = data["Time"]
        manner = data["manner"]
        introduction = data["Introduction"]
        red_packet_type = data["type"]
        rule = data["rule"]

        # 打印活动信息
        print("活动时间:", time)
        print("活动地址:", manner)
        print("活动项目名称:", introduction)
        print("活动类型:", red_packet_type)
        print("活动说明:", rule)

        # 发送PushPlus通知
        token = os.environ.get('tz', '')
        title = '【线报通知】'
        content = f'活动时间: {time}\n活动地址: {manner}\n活动项目名称: {introduction}\n活动类型: {red_packet_type}\n活动说明: {rule}'
        receivers = os.environ.get('RECEIVERS', '').split(',')
        response = send_pushplus_notification(token, title, content, receivers)
        if response.get('code') == 200:
            print('推送通知发送成功')
        else:
            print('推送通知发送失败:', response.get('msg'))

except requests.exceptions.RequestException as e:
    print("网络请求异常:", e)
except (KeyError, ValueError) as e:
    print("JSON解析异常:", e)
except Exception as e:
    print("其他异常:", e)
