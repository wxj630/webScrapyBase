
from selenium import webdriver
import re
import time
import json


str_file = 'anjukeFangjia/cityname.json'

with open(str_file, 'r',encoding="utf-8") as f:
    print("Load str file from {}".format(str_file))
    r = json.load(f)
print(type(r))
print(r)
print(r[0]['pinyin'])


driver = webdriver.Firefox()
for city in r:
    with open('houseprice.txt', 'a+', encoding='utf-8') as f:
        f.write(city['name']+"#")
    for i in range(2009,2019):
        driver.get("https://www.anjuke.com/fangjia/"+str(city['pinyin'].lower())+str(i)+"/")
        houseprice = driver.find_elements_by_css_selector('li.clearfix.up')
        for eachprice in houseprice:
            content = eachprice.find_element_by_tag_name('span')
            finalprice = re.sub("\D", "", content.text)
            for j in range(1,13):
                with open('houseprice.txt', 'a+', encoding='utf-8') as f:
                    finalword =(str(finalprice)+"#")
                    f.write(finalword)
    with open('houseprice.txt', 'a+', encoding='utf-8') as f:
        f.write("\n")