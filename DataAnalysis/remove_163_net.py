import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G = nx.read_pajek('remove_163_net.net',encoding='utf-8')



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

print(G.number_of_selfloops())
for node in G.nodes_with_selfloops():
    print(node)
for edge in G.selfloop_edges():
    print(edge)

G.remove_edge('江映蓉', '江映蓉')
G.remove_edge('PurpleBattery', 'PurpleBattery')

G.remove_parallel_edges()



print(nx.pagerank(G,alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None))





