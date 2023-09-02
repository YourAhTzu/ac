'''
@阿慈 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
corn：10 10 * * *
new Env('所有女生查询');
'''
import requests

env_name = 'syns_data'
env = os.getenv(env_name)

def get_data():
    url = 'https://7.wawo.cc/api/item/wx/launch/mall/un/page'
    headers = {
        'Host': '7.wawo.cc',
        'Connection': 'keep-alive',
        'Authorization': 'env',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x18002831) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx7d1403fe84339669/683/page-frame.html'
    }
    params = {
        'pageNum': '1',
        'pageSize': '12',
        'score': '67',
        'myLevel': '0',
        'sort': '0'
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

def print_data(data):
    records = data['data']['records']
    for item in records:
        name = item['name']
        score_price = item['scorePrice']
        print(f"名称: {name}")
        print(f"积分价格: {score_price}")
        print()

if __name__ == '__main__':
    data = get_data()
    print_data(data)
