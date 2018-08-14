#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/13 13:29
# @Author  : 疏影
# @File    : bjz_login.py

from CashLoanProject.common import config
import requests
import json
from CashLoanProject.common.addSign import Sign

def login_fun():
    url = config.HOST + '/v1/authorizations'
    data = {
        "brushed":"1",
        "deviceModel":"oppor7sm",
        "deviceName":"OPPO",
        "deviceToken":"86787602332210513572489850",
        "memorySize":"32",
        "openudid":"867876023322105",
        "password":"qwe123",
        "phone":"13572489850",
        "systemVersion":"5.1.1"
    }

    s = Sign()
    new_data = s.signfun(data)
    print new_data

    response = requests.post(url=url, headers=config.HEADER_ANDROID, data=new_data,verify=False)
    print response
    token = ''
    if 200 == response.status_code:
        str_content = response.content
        dict_content = json.loads(str_content)
        print 'response:', str_content.decode("unicode-escape")
        if '10000' == dict_content['status']:
            token = dict_content['data']['info']['token']
            print u'当前token:', token
        else:
            print u'获取token失败'
    return token
# 当前token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JqemFwaS41MW1pbmd5YW8uY29tL3YxL2F1dGhvcml6YXRpb25zIiwiaWF0IjoxNTM0MTM4Nzk3LCJleHAiOjc1MzQxMzg3MzcsIm5iZiI6MTUzNDEzODc5NywianRpIjoiM3dsMWt6R214SFBoeHhQVSIsInN1YiI6OTAwMDAwMDA1fQ.G_HY_jLUatekqvMJKpZRjgkiAQwnl2ifr6V3gMg6PMU


if __name__ == '__main__':
    token = login_fun()
    # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JqemFwaS41MW1pbmd5YW8uY29tL3YxL2F1dGhvcml6YXRpb25zIiwiaWF0IjoxNTM0MTM4Nzk3LCJleHAiOjc1MzQxMzg3MzcsIm5iZiI6MTUzNDEzODc5NywianRpIjoiM3dsMWt6R214SFBoeHhQVSIsInN1YiI6OTAwMDAwMDA1fQ.G_HY_jLUatekqvMJKpZRjgkiAQwnl2ifr6V3gMg6PMU'
    # headers = config.HEADER_ANDROID
    # headers.update({'Authorization':'Bearer ' + token})
