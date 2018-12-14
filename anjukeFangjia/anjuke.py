
from selenium import webdriver
import re
import time
import json


str_file = 'cityname.json'

with open(str_file, 'r',encoding="utf-8") as f:
    print("Load str file from {}".format(str_file))
    r = json.load(f)
print(type(r))
print(r)
print(r[0]['pinyin'])


driver = webdriver.Firefox()
for city in r:
    with open('houseprice.csv', 'a+', encoding='utf-8') as f:
        f.write(city['name'])
    for i in range(2018,2008,-1):
        driver.get("https://www.anjuke.com/fangjia/"+str(city['pinyin'].lower())+str(i)+"/")
        for j in range(1,13):
            try:
                houseprice = driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul/li[%s]/a/span' % j)
                finalprice = re.sub("\D", "", houseprice.text)
                with open('houseprice.csv', 'a+', encoding='utf-8') as f:
                    finalword = (','+str(finalprice))
                    f.write(finalword)
            except:
                pass
    with open('houseprice.csv', 'a+', encoding='utf-8') as f:
        f.write("\n")