import csv
from pandas import DataFrame
import pandas as pd
import numpy as np
import numpy

columns = []
with open('Zhaolei_fans.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_1 = [row[0] for row in reader]
    columns.append(list(set(column_1)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_2 = [row[1] for row in reader]
    columns.append(list(set(column_2)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_3 = [row[2] for row in reader]
    columns.append(list(set(column_3)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_4 = [row[3] for row in reader]
    columns.append(list(set(column_4)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_5 = [row[4] for row in reader]
    columns.append(list(set(column_5)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_6 = [row[5] for row in reader]
    columns.append(list(set(column_6)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_7 = [row[6] for row in reader]
    columns.append(list(set(column_7)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_8 = [row[7] for row in reader]
    columns.append(list(set(column_8)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_9 = [row[8] for row in reader]
    columns.append(list(set(column_9)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_10 = [row[9] for row in reader]
    columns.append(list(set(column_10)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_11 = [row[10] for row in reader]
    columns.append(list(set(column_11)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_12 = [row[11] for row in reader]
    columns.append(list(set(column_12)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_13 = [row[12] for row in reader]
    columns.append(list(set(column_13)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_14 = [row[13] for row in reader]
    columns.append(list(set(column_14)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_15 = [row[14] for row in reader]
    columns.append(list(set(column_15)))
with open('Zhaolei_fans.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    column_16 = [row[15] for row in reader]
    columns.append(list(set(column_16)))

song_list=list(set(list(set(column_1))+list(set(column_2))+list(set(column_3))+list(set(column_4))+list(set(column_5))+list(set(column_6))
+list(set(column_7))+list(set(column_8))+list(set(column_9))+list(set(column_10))+list(set(column_11))+list(set(column_12))+list(set(column_13))+list(set(column_14))
+list(set(column_15))+list(set(column_16))))


song_list.remove('')
print(song_list)

one_list=[]


final_matrix=np.zeros((16,31019))


id_list=['1518148','5572309','13941313','30085675','33436583','34037160','37021013','38374651','42628695','54716168','57651700','59189593','59577399','91866735','302906238','349450705']

df=pd.DataFrame(final_matrix,columns=song_list,index=id_list)


print(len(song_list))



for i in list(set(column_1)):
    for j in song_list:
        if i==j:
            df.loc[0,i]=1

for i in list(set(column_2)):
    for j in song_list:
        if i==j:
            df.loc[1,i]=1
for i in list(set(column_3)):
    for j in song_list:
        if i==j:
            df.loc[2,i]=1
for i in list(set(column_4)):
    for j in song_list:
        if i==j:
            df.loc[3,i]=1
for i in list(set(column_5)):
    for j in song_list:
        if i==j:
            df.loc[4,i]=1
for i in list(set(column_6)):
    for j in song_list:
        if i==j:
            df.loc[5,i]=1
for i in list(set(column_7)):
    for j in song_list:
        if i==j:
            df.loc[6,i]=1
for i in list(set(column_8)):
    for j in song_list:
        if i==j:
            df.loc[7,i]=1
for i in list(set(column_9)):
    for j in song_list:
        if i==j:
            df.loc[8,i]=1

for i in list(set(column_10)):
    for j in song_list:
        if i==j:
            df.loc[9,i]=1

for i in list(set(column_11)):
    for j in song_list:
        if i==j:
            df.loc[10,i]=1

for i in list(set(column_12)):
    for j in song_list:
        if i==j:
            df.loc[11,i]=1
for i in list(set(column_13)):
    for j in song_list:
        if i==j:
            df.loc[12,i]=1

for i in list(set(column_14)):
    for j in song_list:
        if i==j:
            df.loc[13,i]=1

for i in list(set(column_15)):
    for j in song_list:
        if i==j:
            df.loc[14,i]=1
for i in list(set(column_16)):
    for j in song_list:
        if i==j:
            df.loc[16,i]=1



df.to_csv('test.csv',encoding='utf-8')

