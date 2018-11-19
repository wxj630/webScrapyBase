#!/usr/bin/python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import lxml


link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers=headers)
# r,resoponde

soup = BeautifulSoup(r.text,"lxml") # 使用beautifulsoup解析这段代码
# 第一篇文章的题目在<h1 class="post-title"><a>。。。。</a>标签内，所以用下面语句提取该博文标题
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)

with open('title_test.txt','w',encoding='utf-8') as f:
    f.write(title)
    f.close()

# 利用字典传递url参数,即params
key_dict= {'key1':'value1','key2':'value2'}
r= requests.get('http://httpbin.org/get',params= key_dict)
print("url已经正确编码：",r.url)
print("字符串方式的响应体：\n",r.text)
