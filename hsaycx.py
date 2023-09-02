import requests
import json
import time

# 发送GET请求获取活动信息
url_activities = 'https://7.wawo.cc/api/live/wx/strategy/activities'
headers = {
    'Host': '7.wawo.cc',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Authorization': 'bearer 632ca4fa-ac13-4a49-8e61-3cb495f2ae04',
    'Content-Type': 'application/json',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x18002831) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wx7d1403fe84339669/683/page-frame.html'
}

response_activities = requests.get(url_activities, headers=headers)

if response_activities.status_code == 200:
    data_activities = response_activities.json()['data']
    if len(data_activities) >= 2:
        for activity in data_activities:
            activity_id = activity['id']
            print('活动ID:', activity_id)

            # 发送POST请求进行预约
            url_appointment = 'https://7.wawo.cc/api/live/wx/strategy/appointment'
            headers_appointment = {
                'Host': '7.wawo.cc',
                'Connection': 'keep-alive',
                'Content-Length': '43',
                'Authorization': 'bearer 632ca4fa-ac13-4a49-8e61-3cb495f2ae04',
                'Content-Type': 'application/json',
                'Accept-Encoding': 'gzip,compress,br,deflate',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x18002831) NetType/WIFI Language/zh_CN',
                'Referer': 'https://servicewechat.com/wx7d1403fe84339669/683/page-frame.html'
            }
            data = {
                'activityId': activity_id,
                'goodsId': 47620,
                'type': 1
            }

            response_appointment = requests.post(url_appointment, headers=headers_appointment, data=json.dumps(data))
            print("预约状态码：", response_appointment.status_code)
            print("预约响应结果：", response_appointment.text)

            if response_appointment.status_code == 200:
                # 预约成功，退出循环
                break

            # 暂停一段时间后再次尝试预约
            time.sleep(5)

    else:
        print('没有活动数据')

else:
    print('请求失败，状态码：', response_activities.status_code)
