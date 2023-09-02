'''
@阿慈 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
corn：10 10 * * *
'''
import requests

# 环境变量
env_name = 'syns_data'
env = os.getenv(env_name)

# 通知相关
message = ""

# 签到函数
def signin():
    signin_url = "https://7.meionetech.com/api/operate/wx/record/signIn"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6945',
        'content-type': 'application/json',
        'authorization': env,
    }
    response = requests.post(signin_url, headers=headers)
    result = response.json()
    if result.get('code') == "000":
        message += "【签到】:签到成功🎉\n"
    else:
        message += f"【签到】:{result.get('message')}\n"

# 预约直播
def live():
    live_url = "https://7.meionetech.com/api/live/wx/strategy/live_appointment/561"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6945',
        'authorization': env,
    }
    response = requests.post(live_url, headers=headers)
    result = response.json()
    if result.get('code') == "000":
        message += f"【预约直播】: {result.get('message')}\n"
    else:
        message += f"【预约直播】:{result.get('message')}\n"

# 浏览积分商城
def viewcust():
    viewcust_url = "https://7.meionetech.com/api/operate/wx/rewards/task/done?taskId=38"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6945',
        'authorization': env,
    }
    data = {
        'taskId': 38
    }
    response = requests.post(viewcust_url, headers=headers, json=data)
    result = response.json()
    if result.get('code') == "000":
        message += "【积分商城】:浏览积分商城成功！\n"
    else:
        message += f"【积分商城】:{result.get('message')}\n"

# 查询积分
def score():
    score_url = "https://7.meionetech.com/api/account/wx/member/assets"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6945',
        'authorization': env,
    }
    response = requests.get(score_url, headers=headers)
    result = response.json()
    if result.get('code') == "000":
        message += f"【积分】:{result.get('data').get('score')}"
    else:
        message += f"【积分】:{result.get('message')}"

# 主程序执行入口
def main():
    # 开始执行日常签到
    signin()
    live()
    viewcust()
    score()
    notify()

# 通知函数
def notify():
    # 发送通知的代码
    print(message)

if __name__ == '__main__':
    main()
