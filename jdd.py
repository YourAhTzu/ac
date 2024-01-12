'''
BY:YourAhTzu
完成日期:1.12 13:10
new Env('金杜丹小程序');
一天一次抓access-token的数据填入jdd变量
'''
import os
import requests
import random
access_token = os.environ.get('jdd')
def sign():
    print(">>>>>开始签到<<<<")
    url = f"https://tianxin.jmd724.com/index.php?store_id=1&r=client/v1/task/sign-up&access_token={access_token}"
    headers = {
        "Host": "tianxin.jmd724.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160043 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Referer": "https://servicewechat.com/wx73f0b52c6da2db74/193/page-frame.html"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if data["code"] == 0:
        print("签到成功", "获得金币数量:", data["data"]["gold_num"])
    else:
        print(data["msg"])

def Article():
    print(">>>>>开始获取文章<<<<<")
    url = f'https://tianxin.jmd724.com/index.php?store_id=1&r=client/v1/article/list&pageNo=1&article_wx_cate_id=0&is_recommend=1&pageSize=10&access_token={access_token}'
    headers = {
        "Host": "tianxin.jmd724.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160043 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Referer": "https://servicewechat.com/wx73f0b52c6da2db74/193/page-frame.html"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    article_list = data["data"]["list"]
    random_ids = random.sample([article["id"] for article in article_list], 3)
    print("获取成功")
    return random_ids

def Share(article_ids):
    print(">>>>>开始分享任务<<<<<")
    for article_id in article_ids:
        url = f'https://tianxin.jmd724.com/index.php?store_id=1&r=client/v1/article/send-task-gold&article_id={article_id}&task_log_type=4&access_token={access_token}'
        headers = {
            "Host": "tianxin.jmd724.com",
            "Connection": "keep-alive",
            "charset": "utf-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160043 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, compress, br, deflate",
            "Referer": "https://servicewechat.com/wx73f0b52c6da2db74/193/page-frame.html"
        }
        response = requests.get(url, headers=headers)
        json_data = response.json()
        msg = json_data["msg"]
        print(f'分享结果:{msg}')

def Collection(article_ids):
    print(">>>>>开始收藏任务<<<<<")
    for article_id in article_ids:
        url = f'https://tianxin.jmd724.com/index.php?store_id=1&r=client/v1/article/send-task-gold&article_id={article_id}&task_log_type=5&access_token={access_token}'
        headers = {
            "Host": "tianxin.jmd724.com",
            "Connection": "keep-alive",
            "charset": "utf-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160043 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, compress, br, deflate",
            "Referer": "https://servicewechat.com/wx73f0b52c6da2db74/193/page-frame.html"
        }
        response = requests.get(url, headers=headers)
        json_data = response.json()
        msg = json_data["msg"]
        print(f'收藏结果:{msg}')

sign()
article_ids = Article()
Share(article_ids)
Collection(article_ids)