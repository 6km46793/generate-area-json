#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#coding:UTF-8

import json
import os
import sys

if os.path.exists('config.json'):
    with open('./config.json', 'r') as f:
        strData = f.read()
        try:
            config = json.loads(strData)
            f.close()
        except BaseException as e:
            print(e)
            print('配置文件格式错误，请确定是否为 json 格式')
            sys.exit()
else:
    print('配置文件读取失败，请确定 ./config.json 是否存在')
    sys.exit()

if os.path.exists('src/allArea_merge.json') and os.path.exists('src/allArea_separate.json'):
    with open('src/allArea_merge.json' if ('merge' in config) and config['merge'] else 'src/allArea_separate.json', 'r') as f:
        strData = f.read()
        try:
            provinceList = json.loads(strData)
            f.close()
        except BaseException as e:
            print(e)
            print('完整的地区数据读取失败，请确定是否为 json 格式')
            sys.exit()
else:
    print('完整的地区数据读取失败，请确定文件是否真实存在')

key = config['key'] if 'key' in config else 'des';
result = []
for item in config['provinceList']:
    temp = {}
    for province in provinceList:
        if (key in province and province[key] == item):
            temp = province
            break
    if temp:
        result.append(temp)
    else:
        print(item,'不在数据列表中，请确定name 或者 code 是否错误')

if 'outputFileName' in config:
    with open('output/' + config['outputFileName'] + '.json', 'w') as f:
        try:
            json.dump(result, f)
            f.close()
            print('json 数据已生成，储存在 “./output/' + config['outputFileName'] + '.json” 中，请自取')
        except BaseException as e:
            print(e)
else:
    print('输出文件配置未配置好，请检查 config.json 中的 outputFileName 配置')
