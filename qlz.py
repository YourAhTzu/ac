'''
@阿慈 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
corn：10 10 * * 
new Env('巧乐兹'); 
119设置抽奖开关
'''
import os
import requests
import time

accessToken = os.getenv("qlz")
pushPlusToken = os.getenv("tz")

share_count = 0  # 已分享次数
lottery_count = 0  # 已抽奖次数
log_message = ""  # 推送日志内容

def signin():
    global log_message
    log_message += "开始执行签到\n"
    url = "https://kapi.yili.com/qlz/api/user/daily/sign?exParams=false"
    headers = {
        "Host": "kapi.yili.com",
        "Connection": "keep-alive",
        "accessToken": accessToken,
        "content-type": "application/x-www-form-urlencoded",
        "scene": "1089",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x1800292e) NetType/4G Language/zh_CN",
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if "bonusPoints" in data:
            log_message += f"获得奖励积分数: {data['bonusPoints']}\n"
        else:
            log_message += "已签到\n"
    except Exception as e:
        log_message += f"签到出现异常: {e}\n"

def share():
    global share_count, log_message
    if share_count >= 10:  # 分享次数达到10次就不再执行
        return
    if share_count == 0:  # 只在第一次执行分享时打印消息
        log_message += "开始执行分享\n"
    url = "https://kapi.yili.com/qlz/api/integral/product/share?productId=0"
    headers = {
        "Host": "kapi.yili.com",
        "Connection": "keep-alive",
        "accessToken": accessToken,
        "content-type": "application/x-www-form-urlencoded",
        "scene": "1089",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x1800292e) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wxa206b57027b01b51/186/page-frame.html",
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if response.status_code == 200 and data["code"] == 200:
            log_message += "分享成功\n"
            share_count += 1  # 已分享次数加一
        else:
            log_message += "分享失败\n"
    except Exception as e:
        log_message += f"分享出现异常: {e}\n"

def lottery():
    global lottery_count, log_message
    if lottery_count >= 3:  # 每天最多抽奖3次
        return
    if lottery_count == 0:  # 只在第一次执行抽奖时打印消息
        log_message += "开始执行抽奖\n"
    url = "https://kapi.yili.com/qlz/api/prize/turntable/draw?exParams=false&refreshTime=300"
    headers = {
        "Host": "kapi.yili.com",
        "Connection": "keep-alive",
        "accessToken": accessToken,
        "content-type": "application/x-www-form-urlencoded",
        "scene": "1089",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x1800292e) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wxa206b57027b01b51/186/page-frame.html",
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if response.status_code == 200 and data["code"] == 200:
            log_message += f"抽奖结果: {data['message']}\n"
            lottery_count += 1  # 已抽奖次数加一
        else:
            log_message += "抽奖失败\n"
    except Exception as e:
        log_message += f"抽奖出现异常: {e}\n"

def push_message(content):
    url = "https://www.pushplus.plus/send"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "token": pushPlusToken,
        "title": "巧乐兹",
        "content": content
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"推送消息响应: {response.text}")
    except Exception as e:
        print(f"推送消息出现异常: {e}")

def main():
    global log_message
    is_signed = False
    for i in range(10):
        if not is_signed:
            signin()
            is_signed = True  # 只在第一次签到时打印信息
        share()
        lottery()
        time.sleep(5)  # 分享和抽奖间隔时间为5秒
    if share_count >= 10:
        log_message += "签到和分享任务已完成。\n"
    if lottery_count >= 3:
        log_message += "抽奖任务已完成。\n"
    push_message(log_message)

if __name__ == '__main__':
    main()
