# -*- coding: utf-8 -*-
# @Time    : 12/31/2020 9:17 PM
# @Author  : Chloe Ouyang
# @FileName: weather_require.py

import requests
import json

KEY = 'FlDExh4G '  # API key(私钥)
UID = "54638815"  # 用户ID, @todo: 当前并没有使用这个值,签名验证方式将使用到这个值

LOCATION = 'beijing'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API = 'https://v0.yiketianqi.com/api'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言


def fetch_weather(location, start=0, days=15):
    result = requests.get(API, params={
        'appid': UID,
        'appsecret': KEY,
        'version': 'v9',
        'city': location
    }, timeout=2)
    return result.json()


def get_weather_by_day(location, day=1):
    result = fetch_weather(location)
    normal_result = {
        "location": result["city"],
        "result": result["data"][day]
    }

    return normal_result


if __name__ == '__main__':
    default_location = "合肥"
    result = fetch_weather(default_location)
    print(json.dumps(result, ensure_ascii=False))

    default_location = "合肥"
    result = get_weather_by_day(default_location)
    print(json.dumps(result, ensure_ascii=False))
