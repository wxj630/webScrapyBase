import csv
import networkx

name_list=[]

for line in open("singer_count.csv", encoding='utf-8'):
    strlist = line.split(',')
    singer_name2 = strlist[1].replace(' ', '')
    events = strlist[2]
    follows = strlist[3]
    fans = strlist[4].strip('\n')
    name_list.append(singer_name2)
print(name_list)

for line in open("all_closeness.csv", encoding='utf-8'):
    strlist = line.split(',')
    singer_id = strlist[0].strip(' ')
    singer_name1 = strlist[1].replace(' ','')
    if singer_name1 not in name_list:
        with open("1609_count.csv","a+",encoding="utf-8") as f:
            f.write(singer_id+","+singer_name1+"\n")


