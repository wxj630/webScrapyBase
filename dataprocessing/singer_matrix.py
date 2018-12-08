import networkx as nx

singer_list=[]
for line in open('signed_artists.csv', encoding='utf-8'):
    strlist = line.split(',')
    x = strlist[0]
    singer_list.append(x)
print(len(singer_list))



for line in open('follows_list.csv', encoding='utf-8'):
    strlist = line.split(',')
    y = strlist[1]
    if y in singer_list:
        with open('follows_list2.csv','a+',encoding='utf-8') as f:
            f.write(line)
    else:
        pass


# def createGraph(filename, w_index):
#     G = nx.DiGraph()
#     for line in open(filename,encoding='utf-8'):
#         strlist = line.split(',')
#         n1 = strlist[0]
#         n2 = strlist[1]
#         #weight = float(strlist[w_index])
#         G.add_edges_from([(n1, n2)])
#     return G
# G=createGraph('follow_list2.csv',2)