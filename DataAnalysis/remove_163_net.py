import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()

G = nx.read_pajek('follow_at_matrix3.net',encoding='utf-8')
# nx.draw(G,with_labels=True)
# plt.show()
G.remove_node('网易云音乐')
nx.write_pajek(G,'remove_163_net.net')

print('节点数：'+str(G.number_of_nodes()))
print('边数'+str(G.number_of_edges()))
print('网络密度'+str(nx.density(G)))

d=nx.degree(G)
d1=sorted(d,key=lambda x:x[1],reverse=True)
d2=d1[0:10]
print('度值前10:'+str(d2))


e=G.in_degree()
e1=sorted(e,key=lambda x:x[1],reverse=True)
e2=e1[0:10]
print('入度前10:'+str(e2))

f=G.out_degree()
f1=sorted(f,key=lambda x:x[1],reverse=True)
f2=f1[0:10]
print('出度前10:'+str(f2))



