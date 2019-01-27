# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# import time
# from selenium.webdriver.common.action_chains import ActionChains
#
# ff_option = Options()
# # ff_option.add_argument('-headless')
#
# fp = webdriver.FirefoxProfile()
# fp.set_preference('permissions.default.image', 2)
# fp.set_preference('plugin.state.flash',2)
# # fp.set_preference("permissions.default.stylesheet", 2)
#
# driver = webdriver.Firefox(firefox_profile=fp,options=ff_option)
# driver.get("http://open.nlc.cn/onlineedu/course/explore/search.htm")
#
# for i in range(1,77):
#     courses_name = driver.find_elements_by_css_selector('a.link-dark')
#     courses_id = driver.find_elements_by_css_selector('a.link-dark')
#     watchs_num = driver.find_elements_by_css_selector('span.num')
#     for course_name,course_id,watch_num in zip(courses_name,courses_id,watchs_num):
#         with open('courses_id.csv', 'a+', encoding='utf-8') as f:
#             f.write(course_name.text+','+course_id.get_attribute('href')+','+watch_num.text+'\n')
#     next_page=driver.find_element_by_css_selector('a.nextPage')
#     next_page.click()

# url_list = []
# name_list = []
# for line in open("courses_id.csv", encoding='utf-8'):
#     strlist = line.split(',')
#     name = strlist[0]
#     url = strlist[1]
#     watch = strlist[2].strip('\n')
#
#     driver.get(url)
#     start_learn = driver.find_element_by_xpath('//*[@id="joincourse"]')
#     start_learn.click()
#
#     titles = driver.find_elements_by_css_selector('span.title')
#     dates = driver.find_elements_by_css_selector('span.date')
#     for title,date in zip(titles,dates):
#         with open('courses_date.csv', 'a+', encoding='utf-8') as f:
#             f.write(name+','+url+','+watch+','+title.text+','+date.text+'\n')

# for i in range(1,75):
#     driver.get('http://www.namoc.org/Videos/zxxx/msgjt/index_'+str(i)+'.htm')
#     courses_name = driver.find_elements_by_css_selector('font')
#     courses_time = []
#     for i in range(1,6):
#         course_time = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[1]/div[1]/ul/li[%s]/div/span'%i)
#         courses_time.append(course_time)
#         print(course_time.text)
#     for course_name,course_time in zip(courses_name,courses_time):
#         with open('art_mesume.csv', 'a+', encoding='utf-8') as f:
#             f.write(course_name.text+','+course_time.text+'\n')

hour = []
min = []
second = []
for line in open("art_mesume.csv", encoding='utf-8'):
    strlist = line.split(',')
    name = strlist[0]
    video_time = strlist[1].strip('\n')
    strlist2 = video_time.split(':')
    if len(strlist2) == 3:
        hour.append(int(strlist2[0]))
        min.append(int(strlist2[1]))
        second.append(int(strlist2[2]))
    else:
        hour.append(0)
        min.append(int(strlist2[0]))
        second.append(int(strlist2[1]))
print(hour)
print(min)
print(second)

print(sum(hour))
print(sum(min))
print(sum(second))

st = '24:11015:10088'
def t2s(t):
    h,m,s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

print(t2s(st))

print(11015/60)
print(757388/3600)
