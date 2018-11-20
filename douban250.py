#!/usr/bin/python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import lxml

def get_movies():
    headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
    'Host': 'movie.douban.com'
                }
    movie_list=[]
    director_list=[]
    for i in range(0,10):
       link='https://movie.douban.com/top250?start='+str(i*25)
       r=requests.get(link,headers=headers,timeout=10)
       print(str(i+1),'页相应状态码：',r.status_code)
       # print(r.text)

       soup=BeautifulSoup(r.text,'lxml')
       # movie name in <div class='hd'><span class='titile>
       div_list=soup.find_all('div',class_='hd')
       div_director=soup.find_all('div',class_='bd')
       for each in div_list:
           # extract movie name from <span>
           movie=each.a.span.text.strip()
           movie_list.append(movie)
    return movie_list

'''
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
       div_director=soup.find_all('div',class_='bd')
       for each in div_director:
           # extract movie name from <span>
           director=each.a.p.text.strip()
           director_list.append(director)
    return director_list
'''

movies=get_movies()
print(movies)

# directors=get_mdirector()
# print(directors)
