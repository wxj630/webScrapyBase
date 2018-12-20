
from selenium import webdriver
import re
'''
抚州 
平顶山
六安 luan
'''


driver = webdriver.Firefox()

with open('houseprice_single.csv', 'a+', encoding='utf-8') as f:
    f.write("吉林"+",")
for i in range(2018,2008,-1):
    driver.get("https://www.anjuke.com/fangjia/jilin"+str(i)+"/")
    for j in range(1,13):
        houseprice = driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul/li[%s]/a/span' % j)
        print(houseprice.text)
        finalprice = re.sub("\D", "", houseprice.text)
        with open('houseprice_single.csv', 'a+', encoding='utf-8') as f:
            finalword =(str(finalprice)+",")
            f.write(finalword)
with open('houseprice_single.csv', 'a+', encoding='utf-8') as f:
    f.write("\n")