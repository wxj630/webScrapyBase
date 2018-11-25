
from selenium import webdriver
import re
import time

driver = webdriver.Firefox()
for i in range(2009,2019):

    driver.get("https://www.anjuke.com/fangjia/beijing"+str(i))
    houseprice = driver.find_elements_by_css_selector('li.clearfix.up')
    for eachprice in houseprice:
        content = eachprice.find_element_by_tag_name('span')
        finalprice = str(re.findall(r"\d+\.?\d*", content.text))
        for j in range(1,13):
            with open('houseprice.txt', 'a+', encoding='utf-8') as f:
                finalword =(str(i)+"年#"+str(j)+"月#"+ finalprice+"\n")
                f.write(finalword)
                f.close()
