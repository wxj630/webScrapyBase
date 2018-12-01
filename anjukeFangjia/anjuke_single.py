
from selenium import webdriver
import re
'''
厦门 xm
长春 cc
长沙 cs
'''


driver = webdriver.Firefox()

with open('houseprice_single.txt', 'a+', encoding='utf-8') as f:
    f.write("平顶山"+"#")
for i in range(2009,2019):
    driver.get("https://www.anjuke.com/fangjia/pingdingsha"+str(i)+"/")
    houseprice = driver.find_elements_by_css_selector('li.clearfix.up')
    for eachprice in houseprice:
        content = eachprice.find_element_by_tag_name('span')
        finalprice = re.sub("\D", "", content.text)
        for j in range(1,13):
            with open('houseprice_single.txt', 'a+', encoding='utf-8') as f:
                finalword =(str(finalprice)+"#")
                f.write(finalword)
with open('houseprice_singe.txt', 'a+', encoding='utf-8') as f:
    f.write("\n")