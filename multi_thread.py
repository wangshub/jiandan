作者：tonnie
链接：https://zhuanlan.zhihu.com/p/25228075
来源：知乎
著作权归作者所有，转载请联系作者获得授权。

#-*- coding:utf-8 -*-
import requests
from lxml import etree
from time import time
from threading import Thread

url = 'https://movie.douban.com/top250'

def fetch_page(url):
    response = requests.get(url)
    return response

def parse(url):
    response = fetch_page(url)
    page = response.content
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    for p in pages:
        fetch_list.append(url + p.get('href'))

    def fetch_content(url):
        response = fetch_page(url)
        page = response.content
        html = etree.HTML(page)
        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

    threads = []
    for url in fetch_list:
        t = Thread(target=fetch_content, args=[url])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
        # print(i, title)
