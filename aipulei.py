from selenium import webdriver

driver = webdriver.Firefox()
for i in range(35210,48898):

    driver.get("http://retractiondatabase.com/撤稿查询/aid/2"+str(i)+"/mid/447")
    url=str("http://retractiondatabase.com/撤稿查询/aid/2"+str(i)+"/mid/447")

    tit = driver.find_element_by_id('article_title')
    content = tit.find_element_by_tag_name('h1')
    title = content.text

    oriurl = driver.find_element_by_css_selector('a.btn.btn-large.btn-primary')
    content3 = oriurl.get_attribute('href')
    url2 = str(content3)

    infos = driver.find_elements_by_class_name('list-group-item-text')
    with open('aipulei5.txt', 'a+', encoding='utf-8') as f:
        f.write(title+"#"+url+"#"+url2+"#")


    for info in infos:
        if info.text is None:
            content2 = "N/A"
        else:
            content2 = info.text
        with open('aipulei5.txt', 'a+', encoding='utf-8') as f:
            f.write(content2+"#")

    with open('aipulei5.txt', 'a+', encoding='utf-8') as f:
        f.write("\n")



