from selenium import webdriver
from selenium.webdriver.firefox.options import Options



for line in open("signed_artists.csv", encoding='utf-8'):
    strlist = line.split(',')
    artist_name = strlist[0].replace(' ', '')
    artist_id = strlist[1]
    user_id = strlist[2]

    ff_option = Options()
    ff_option.add_argument('-headless')

    fp = webdriver.FirefoxProfile()
    fp.set_preference('permission.default.image', 2)
    fp.set_preference("permission.default.stylesheet", 2)

    driver = webdriver.Firefox(firefox_profile=fp,options=ff_option)
    driver.get("https://music.163.com/#/artist?id="+str(artist_id))
    driver.switch_to.frame('g_iframe')
    next_page=driver.find_element_by_xpath('//*[@id="m_tabs"]/li[4]/a')
    next_page.click()
    try:
        singer_intro = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/p')
        with open('singer_intro.txt', 'a+', encoding='utf-8') as f:
            f.write(artist_id+"#"+artist_name+"#"+singer_intro.text+"\n")
    except:
        with open('singer_intro.txt', 'a+', encoding='utf-8') as f:
            f.write(artist_id+"#"+artist_name+"#"+"没有艺人介绍"+"\n")