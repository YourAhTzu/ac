''' 
new Env('小米运动');
"账号&密码&最小步数&最大步数"多号#隔开
PS:请勿频繁调用接口不然封IP调用(接口调用于七七大佬API)
'''
import os
import requests

url = "http://api.xn--7gqa009h.top/api/xmbs2"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36"
}

xmyd = os.environ.get("xmyd")
if xmyd:
    params = xmyd.split("#")
    for param in params:
        user, password, step_min, step_max = param.split("&")
        payload = {
            "user": user,
            "password": password,
            "step_min": step_min,
            "step_max": step_max
        }
        response = requests.post(url, data=payload, headers=headers)
        print(response.text)
else:
    print("环境变量xmyd不存在")