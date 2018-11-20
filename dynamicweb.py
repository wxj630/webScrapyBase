import requests
import json

def single_page_comment(link):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r = requests.get(link, headers= headers)
    #print (r.text)

    # 获取 json 的 string
    json_string = r.text
    # 只提取字符串中符合json格式的部分
    json_string = json_string[json_string.find('{'):-2]

    # json.loads()把字符串格式的数据转化为json数据
    json_data = json.loads(json_string)
    # 提取评论列表
    comment_list = json_data['results']['parents']

    for eachone in comment_list:
        message = eachone['content']
        print (message)

for page in range(1,5):
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery112403473268296510956_1531502963311&limit=10&offset="
    link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1531502963316"
    page_str = str(page)
    link = link1+page_str+link2
    print(link)
    single_page_comment(link)