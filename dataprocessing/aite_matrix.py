import networkx as nx

# singer_list=[]
# for line in open('signed_artists.csv', encoding='utf-8'):
#     strlist = line.split(',')
#     x = strlist[0]
#     singer_list.append(x)
# print(len(singer_list))
#
#
#
# for line in open('artists_in_events.csv', encoding='utf-8'):
#     strlist = line.split(',')
#     x = strlist[0]
#     y = strlist[1]
#     if y in singer_list:
#         if x != y:
#             with open('artists_in_events2.csv','a+',encoding='utf-8') as f:
#                 f.write(line)
#         else:
#             pass
#     else:
#         pass
#
#
# def createGraph(filename, w_index):
#     G = nx.DiGraph()
#     for line in open(filename,encoding='utf-8'):
#         strlist = line.split(',')
#         n1 = '\"'+strlist[0]+'\"'
#         n2 =  '\"'+strlist[1]+'\"'
#         #weight = float(strlist[w_index])
#         G.add_edges_from([(n1, n2)])
#     return G
# G=createGraph('artists_in_events2.csv',2)
# nx.write_pajek(G,'artists_in_events2.net')

# G = nx.DiGraph()
# G2 = nx.DiGraph()
# for line in open('follows_list2.csv',encoding='utf-8'):
#     strlist = line.split(',')
#     n1 = '\"'+strlist[0]+'\"'
#     n2 =  '\"'+strlist[1]+'\"'
#     #weight = float(strlist[w_index])
#     with open('follow_at_matrix.csv', 'a+', encoding='utf-8') as f:
#         f.write(n1+','+n2+'\n')
#     G.add_edges_from([(n1, n2)])
# for line in open('artists_in_events2.csv',encoding='utf-8'):
#     strlist = line.split(',')
#     n1 = '\"'+strlist[0]+'\"'
#     n2 =  '\"'+strlist[1]+'\"'
#     #weight = float(strlist[w_index])
#     with open('follow_at_matrix.csv', 'a+', encoding='utf-8') as f:
#         f.write(n1 +','+ n2+'\n')
#     G.add_edges_from([(n1, n2)])


# def createGraph(filename, w_index):
#     G = nx.DiGraph()
#     for line in open(filename,encoding='utf-8'):
#         strlist = line.split(',')
#         n1 = '\"'+strlist[0]+'\"'
#         n2 =  '\"'+strlist[1]+'\"'
#         #weight = float(strlist[w_index])
#         G.add_edges_from([(n1, n2)])
#     return G
# G=createGraph('artists_in_events2.csv',2)
# nx.write_pajek(G,'artists_in_events2.net')

# line_list=[]
# line_set=[]
# cnt=0
# for line in open('follow_at_matrix.csv',encoding='utf-8'):
#     line_list.append(line)
# line_set = list(set(line_list))
#
# for line1 in line_set:
#     for line2 in line_list:
#         if line1==line2:
#             cnt=cnt+1
#             strlist = line1.split(',')
#             n1 = strlist[0].strip('\n')
#             n2 = strlist[1].strip('\n')
#             with open('follow_at_matrix3.csv', 'a+', encoding='utf-8') as y:
#                 y.write(n1+','+str(cnt)+','+n2+'\n')
#     cnt = 0

# line_list=[]
# sum_n_list=[]
# n_list=[]
# w_list=[]
# for line in open('follow_at_matrix.csv',encoding='utf-8'):
#     line_list.append(line)
# line_set = list(set(line_list))
# for line in open('follow_at_matrix2.csv',encoding='utf-8'):
#     strlist = line.split(',')
#     n1 = strlist[0]
#     n2 = strlist[2]
#     n3 = strlist[1]
#     w_list.append(int(n3))
#
# w_set= sorted(set(w_list))
# print(w_set)
# print(sorted(w_list))
# print(len(w_list))

# w2_list=[]
# for line in open('follow_at_matrix2.csv', encoding='utf-8'):
#     strlist = line.split(',')
#     n1 = strlist[0]
#     n2 = strlist[2]
#     n3 = strlist[1]
#     if int(n3)==2:
#         w2_list.append([n1,n2])
#
# for line in open('follow_at_matrix2.csv', encoding='utf-8'):
#     strlist = line.split(',')
#     n1 = strlist[0]
#     n2 = strlist[2]
#     n3 = int(strlist[1])
#     for w2_elem in w2_list:
#         if n1==w2_elem[0] and n2==w2_elem[1] and n3==1:
#             pass
#         with open('follow_at_matrix3.csv', 'a+', encoding='utf-8') as y:
#             y.write(line)












def createGraph(filename, w_index):
    G = nx.DiGraph()
    for line in open(filename,encoding='utf-8'):
        strlist = line.split(',')
        n1 = strlist[0].strip('\n')
        n2 = strlist[2].strip('\n')
        n3 = int(strlist[1])
        #weight = float(strlist[w_index])
        G.add_edges_from([(n1,n2)],weight=n3)
    return G
G=createGraph('follow_at_matrix3.csv',2)
nx.write_pajek(G,'follow_at_matrix3.net')