#抓ck要PHPSESSID=后的数据变量wmj
import requests
import os

def hbdh():
    print("开始执行红包兑换任务")
    url = "http://app.weimi99.cn/index/everyday/score_hb.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; V2068A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/16.9.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://cdnshare.weimi99.cn/index/user/index.html",
        "Cookie": "PHPSESSID=" + os.environ.get("wmj")
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        msg = json_data.get("msg")
        print("红包兑换结果:", msg)
    else:
        print("请求失败")
        
def sign():
    print("开始执行签到任务")
    url = "http://cdnshare.weimi99.cn/index/everyday/punch.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; V2068A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/16.9.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://cdnshare.weimi99.cn/index/user/index.html",
        "Cookie": "PHPSESSID=" + os.environ.get("wmj")
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        msg = json_data.get("msg")
        print("签到结果:", msg)
    else:
        print("请求失败")

def main():
    sign()
    hbdh()

main()
