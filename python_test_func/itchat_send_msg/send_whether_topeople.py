#!/home/mengde/.virtualenvs/lianxi/bin/python

import json
import re
import time
from datetime import datetime, timedelta

import itchat
import requests


def get_weather(city):
    """获取天气"""
    url = "http://wthrcdn.etouch.cn/weather_mini?city=" + city
    response = requests.get(url)
    data = json.loads(response.text)['data']['forecast'][1]
    ganmao = json.loads(response.text)['data']['ganmao']
    fengli = data['fengxiang'] + " " + re.findall(r'CDATA\[(.*?)\]', data['fengli'])[0]
    date_month = (datetime.now() + timedelta(days=1)).strftime("%Y年%m月")
    info = "明天是%s%s,\n最%s,\n最%s,\n%s,\n%s,\n%s" % \
           (date_month, data['date'], data['high'], data['low'], data['type'], fengli, ganmao)
    if '雨' in data['type']:
        info += ",\n千万不要忘记带雨伞哦!!!"
    elif "晴" in data['type']:
        info += ",\n一定要注意防晒啊!!!"
    return info


def send_message(name, data):
    """发送消息"""
    friend = itchat.search_friends(name=name)
    username = friend[0]['UserName']
    itchat.send(data, toUserName=username)


if __name__ == "__main__":
    print("开始发送消息")
    # 登录
    itchat.auto_login(hotReload=True)
    while True:
        # 运行时间将在什么时候发送消息
        if datetime.now().hour == 21 and datetime.now().minute == 0:
            print(datetime.now())
            # 输入要发送的人在你好友列表里的备注和你想要发送天气的城市,以数组形式发送
            data = [("张三", "北京")]
            for info in data:
                wether_info = get_weather(info[1])
                send_message(info[0], wether_info)
            time.sleep(60)
        else:
            time.sleep(60)
