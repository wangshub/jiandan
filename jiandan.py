#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import os
from Download import request
import thread

class jiandan():
    def get(self, url):
        html = request.get(url, 3)
        return html.text
    def save(self, url):
        html = self.get(url)
        soup = BeautifulSoup(html, 'lxml')
        tag_all = soup.find_all('div', class_='text')
        for tag in tag_all:
            img_url =  tag.find('img')['src']

            if cmp(img_url[0:5],'http:'):
                img_url = img_url[7:]
            elif cmp(img_url[0:2], '////'):
                img_url = img_url[2:]
            else :
                continue

            [filename, filetype] = img_url.split('/')[-1].split('.')
            with open('/media/wangs/Docs/pic/jiandan/{}.{}'.format(filename, filetype), 'wb') as img:
                img.write(request.get('http://'+img_url, 3).content)
                img.close()



for i in range(3, 2353):
    url = 'http://jandan.net/ooxx/page-{}#comments'.format(i)
    print url
    jd = jiandan()
    jd.save(url)
