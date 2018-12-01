from selenium import webdriver
import selenium.webdriver.support.ui as ui
import traceback

def catchSongs(url_id,url):

    user = url_id.split('=')[-1].strip()
    print('excute user:',user)

    driver = webdriver.Firefox()#,executable_path='/Users/mrlevo/phantomjs-2.1.1-macosx/bin/phantomjs')
    #  注意填上路径
    driver.get(url)

    driver.switch_to.frame('g_iframe')  # 网易云的音乐元素都放在框架内！！！！先切换框架

    songs_content = driver.find_element_by_xpath('//*[@class="j-flag"]/table/tbody')
    song_key = 1
    wrong_time = 0
    while wrong_time < 5:  # 不断获取歌信息，假定5次获取不到值，就判无值可获取，跳出循环
        songs = driver.find_element_by_xpath('//*[@class="j-flag"]/table/tbody/tr[%s]'%song_key)
        song_name = songs.find_element_by_css_selector("b").get_attribute("title")
        song_time = songs.find_element_by_css_selector("span.u-dur ").text
        song_singer = songs.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[%s]/td[4]/div/span"%song_key).get_attribute("title")
        song_album = songs.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[%s]/td[5]/div/a"%song_key).get_attribute("title")
        new_line = song_name+song_time+song_singer+song_album

        song_key +=1
        print(new_line)





if __name__ == '__main__':
    url = 'http://music.163.com/user/home?id=355488332'
    playlist_url = 'https://music.163.com/#/playlist?id=504871154'
    catchSongs(url,playlist_url)

