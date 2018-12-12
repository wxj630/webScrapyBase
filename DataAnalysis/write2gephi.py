import networkx as nx

G=nx.read_pajek('follow_at_matrix3.net')
nx.write_gexf(G,'follow_at_matrix3.gexf',encoding='utf-8')

G=nx.read_pajek('remove_163_net.net')
nx.write_gexf(G,'remove_163_net.gexf',encoding='utf-8')