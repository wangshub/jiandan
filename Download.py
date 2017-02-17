#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import os
import re
import random
import time
class Download():
    def __init__(self):
        # ip list
        self.iplist = []
        iphtml = requests.get("http://haoip.cc/tiqu.htm")
        iplist_reg = re.findall(r'\d+\.\d+.\d+.\d+:\d+', iphtml.text, re.S)
        for ip in iplist_reg:
            self.iplist.append(ip.strip())
        # print self.iplist
        # browser user agent list
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

    def get(self, url, timeout, proxy = None, num_retry = 6):
        UA = random.choice(self.user_agent_list)
        headers = {'User-Agent': UA}

        if (proxy == None):
            try:
                response = requests.get(url, headers=headers, timeout = timeout)
                return response
            except:
                if num_retry > 0:
                    print 'sleep , and retry'
                    time.sleep(1)
                    return self.get(url, timeout, num_retry-1)
                else:
                    print 'slepp , and begin to use proxy'
                    tie.sleep(1)
                    IP = ''.join(random.choice(self.iplist))
                    proxy = {'http':IP}
                    return self.get(url, timeout, proxy)

        else:
            try:
                IP = ''.join(random.choice(self.iplist))
                proxy = {'http': IP}
                response = requests.get(url, headers = headers, proxies = proxy, timeout = time)
                return response
            except:
                if num_retry > 0:
                    time.sleep(1)
                    print 'change another proxy'
                    IP = ''.join(random.choice(self.iplist))
                    proxy = {'http': IP}
                    print IP
                    return self.get(url,timeout, proxy, num_retry-1)
                else:
                    print 'proxy is broken !'
                    return self.get(url, 3)

request = Download()
