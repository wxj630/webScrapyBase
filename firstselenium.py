from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
# 因为评论在iframe中，所以要用.frame对iframe进行解析
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))

'''
for x in range(4):
        next_page=driver.find_element_by_class_name('more-btn')
        next_page.click()
'''

# 再通过find elements by css selector找到'div.reply-content'
comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print(content.text)
