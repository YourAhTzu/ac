"""
new Env('申工社');
微信公众号:申工社抓fwdt.shengongshe.org的token变量名称:sgs多账号@分开
诺打印token失效就抓签到的token
"""
import requests
import os

tokens = os.environ.get("sgs").split("@") 

def sign(token):
    url = "https://fwdt.shengongshe.org/sgsWchartApi/api/My/sign"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2f) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Token": token
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    msg = data["msg"]
    print("签到结果:", msg)
    
def get_media_ids(token):
    url = 'https://fwdt.shengongshe.org/sgsWchartApi/api/ImageText/list'
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2f) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Token": token
    }
    params = {
        'page': 1,
    }

    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        news_list = data['news']
        media_ids = []
        for news in news_list:
            media_id = news['media_id']
            media_ids.append(media_id)
        return media_ids[:3]

def execute_url(token, media_id):
    url = "https://fwdt.shengongshe.org/sgsWchartApi/api/ImageText/read"
    headers = {
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Origin": "https://fwdt.shengongshe.org",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2f) NetType/WIFI Language/zh_CN",
        "Token": token
    }
    data = {
        "media_id": media_id
    }

    response = requests.post(url, headers=headers, data=data)
    json_data = response.json()
    msg = json_data["msg"]
    print(f"运行结果：{msg}")

if __name__ == "__main__":
    print("开始签到")
    for token in tokens:
        sign(token)
        media_ids = get_media_ids(token)
        print("开始执行阅读任务")
        for media_id in media_ids:
            execute_url(token, media_id)
        print("====================================")  