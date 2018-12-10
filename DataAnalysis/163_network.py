import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_pajek('follow_at_matrix3.net',encoding='utf-8')
# nx.draw(G,with_labels=True)
# plt.show()

print(G.number_of_nodes())
print(G.number_of_edges())
print(nx.density(G))
d=nx.degree(G)
d1=sorted(d,key=lambda x:x[1],reverse=True)
d2=d1[0:10]
print(d2)