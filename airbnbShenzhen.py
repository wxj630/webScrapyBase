from selenium import webdriver
import time

driver = webdriver.Firefox()
for i in range(1,21):
    driver.get("https://zh.airbnb.com/s/Shenzhen--China?page="+str(i))
    rent_list = driver.find_elements_by_css_selector('')
    for eachhouse in rent_list:
        comment=eachhouse.find_element_by_css_selector('')
        comment=comment.text
        price=eachhouse.find_element_by_css_selector('')


