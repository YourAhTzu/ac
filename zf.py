'''
玩法贼简单，每天看十个广告得0.2锁定金每天凌晨分红
推广两代收益 1级30% 2级20%  10r起提类似于资金盘
注册链接：http://lses-lcae.ihuju.cn/index.php/Home/Public/reg/recom/317577
环境变量名字zf填ck
new Env('众分');
'''

import time
import random
import requests
import os

env_name = 'zf' 
env = os.getenv(env_name)

url = "http://lses-lcae.ihuju.cn/index.php/Home/Index/ad_video_api.html"
headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Cookie': env,
}
data = {
    "uid": "53356"
}

for i in range(10):
    delay = random.randint(30, 50)

    response = requests.post(url, headers=headers, data=data)
    json_data = response.json()

    status = json_data["status"]

    if status == 1:
        
        print(f"第{i+1}次观看广告")
        print("观看成功！")
        
    elif status == 0:
        
        print("视频全部观看完毕，停止运行！")
        break
        
    time.sleep(delay)
