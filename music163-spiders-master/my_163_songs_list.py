# -*- coding: utf-8 -*-

import traceback
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random


# 存储为文本的子函数
def write2txt(data,path):
    with open(path,"a+",encoding="utf-8") as f:
        f.write(data+"\n")
        f.close()


# 获取该id喜欢音乐的列表
def catchSongs(url_id,url):

    user = url_id.split('=')[-1].strip()
    print('excute user:',user)

    driver = webdriver.Firefox()#,executable_path='/Users/mrlevo/phantomjs-2.1.1-macosx/bin/phantomjs')
    #  注意填上路径
    driver.get(url)

    driver.switch_to.frame('g_iframe')  # 网易云的音乐元素都放在框架内！！！！先切换框架

    try:
        song_key = 1
        wrong_time = 0
        while wrong_time < 5:  # 不断获取歌信息，假定5次获取不到值，就判无值可获取，跳出循环
            try:
                songs = driver.find_element_by_xpath('//*[@class="j-flag"]/table/tbody/tr[%s]' % song_key)
                song_name = songs.find_element_by_css_selector("b").get_attribute("title")
                song_time = songs.find_element_by_css_selector("span.u-dur ").text
                song_singer = songs.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[%s]/td[4]/div/span" % song_key).get_attribute(
                    "title")
                song_album = songs.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[%s]/td[5]/div/a" % song_key).get_attribute(
                    "title")
                new_line = song_name +"#" + song_time +"#"+ song_singer+"#" + song_album
                # info_ = songs[0].get_attribute(song_name,song_time,song_singer,song_album)
                # info_ = songs[0].text.strip().split("\n")
                # if len(info_) == 5:
                #     info_.insert(2,'None') # 没有MV选项的进行插入None
                # new_line = '%s|'%user+'|'.join(info_)

                song_key +=1
                #new_line = "%s|%s|%s|%s|%s|%s|%s"%(user,info_[0],info_[1],info_[2],info_[3],info_[4],info_[5])

                print(new_line)

                write2txt(new_line,user)

                # mac写入文件需要改变字符，以id命名的文件，存储在执行脚本的当前路径下，
                # 在win下请去掉编.endcode('utf-8')


            except Exception as ex:
                wrong_time +=1
                # print ex
    except Exception as ex:
        pass

    finally:
        # driver.quit()
        pass



# 获取id所喜爱的音乐的url
def catchPlaylist(url):


    driver = webdriver.Firefox()
    #,executable_path='/Users/mrlevo/phantomjs-2.1.1-macosx/bin/phantomjs')
    #  注意填上路径
    driver.get(url)

    driver.switch_to.frame('g_iframe')  # 网易云的音乐元素都放在框架内！！！！先切换框架

    try:
        wait = ui.WebDriverWait(driver,15)
        wait.until(lambda driver: driver.find_element_by_xpath('//*[@class="m-cvrlst f-cb"]/li[1]/div/a'))
        # 根据xpath获取元素

        urls = driver.find_elements_by_xpath('//*[@class="m-cvrlst f-cb"]/li/div/a')
        favourite_url = urls[0].get_attribute("href")
        urls_list = []
        for i in range(len(urls)):
            urls_list.append(urls[i].get_attribute("href"))

    except Exception as ex:
        traceback.print_exc()
    finally:
        driver.quit()
    # print favourite_url
    return urls_list



if __name__ == '__main__':

    for url in ['http://music.163.com/user/home?id=355488332']:
        url_playlist = catchPlaylist(url)
        print(url_playlist)
        # 这里把自己的id替换掉，想爬谁的歌单都可以，只要你有他的id
        for i in range(len(url_playlist)):
            time.sleep(random.randint(0, 1)) # 随机休眠时间0~1秒
            catchSongs(url, url_playlist[i])