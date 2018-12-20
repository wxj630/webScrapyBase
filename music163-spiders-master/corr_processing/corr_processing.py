import csv
import networkx

for line in open("closeness.csv", encoding='utf-8'):
    strlist = line.split(',')
    name1 = strlist[1].replace(' ','')
    outdegree = strlist[5].replace('\n','')
    for line in open("events_follows_fans_num.csv", encoding='utf-8'):
        strlist = line.split(',')
        name2 = strlist[0].replace(' ','')
        events = strlist[1]
        follows = strlist[2]
        fans = strlist[3].strip('\n')

        if name1==name2:
            with open("outcloseness_count.csv","a+",encoding="utf-8") as f:
                f.write(name1+","+outdegree+","+events+","+follows+","+fans+"\n")


