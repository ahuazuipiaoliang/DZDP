# -*- coding: UTF-8 -*-

'''
全网代理IP Created on 2016年12月23日
@author: www.goubanjia.com
'''

import urllib;\
import random


# 这里填写全网代理IP提供的API订单号（请到用户中心获取）
order = "bb8932ed9a66d49b5d16dfc1cf471a04";
# 获取IP的API接口
apiUrl = "http://dynamic.goubanjia.com/dynamic/get/" + order + ".html";
# 要抓取的目标网站地址
targetUrl = "http://1212.ip138.com/ic.asp";

try:
    # 获取IP列表
    res = urllib.urlopen(apiUrl).read().strip("\n");
    # 按照\n分割获取到的IP
    ips = res.split("\n");
    # 随机选择一个IP
    proxyip = random.choice(ips)
    # 使用代理IP请求目标网址
    html = urllib.urlopen(targetUrl, proxies={'http': 'http://' + proxyip})
    # 输出内容
    print("使用代理IP " + proxyip + " 获取到如下HTML内容：\n")
except Exception:
    print(Exception.args)