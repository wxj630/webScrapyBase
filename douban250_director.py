#!/usr/bin/python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import lxml

def get_mdirector():
    headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
    'Host': 'movie.douban.com'
                }
    director_list=[]
    for i in range(0,10):
       link='https://movie.douban.com/top250?start='+str(i*25)
       req=requests.get(link,headers=headers,timeout=10)
       print(str(i+1),'页相应状态码：',req.status_code)
       # print(r.text)

       soup=BeautifulSoup(req.text,'lxml')
       # director name in <div class='bd'><span class='titile>
       div_director=soup.find_all('span',class_='rating_num')
       for each in div_director:
           # extract movie name from <span>
           director=each.text.strip() # 没有<a>标签所以不用a.
           director_list.append(director)
    return director_list


directors=get_mdirector()
print(directors)
