import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import csv


csv_file = pd.read_csv('final_matrix2.csv')
df = pd.DataFrame(csv_file)
df2=df.fillna(0)
df3=df2.T

# df3.to_excel('final_matrix2.xlsx')

# nx.write_pajek(df,'pajek.net')

# df4 = pd.DataFrame(np.dot(df2,df3))

# df4.to_excel('usr_matrix.csv')

df5 = pd.DataFrame(np.dot(df3,df2))
# df5.to_csv('song_matrix.csv')

# G = nx.from_pandas_adjacency(df4)
# print(list(G.nodes))
# print(list(G.edges))
# print(df4)
# nx.draw(G,with_labels=True)
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
# plt.show()
# nx.write_pajek(G,'usr_matrix.net')

# G2 = nx.from_pandas_adjacency(df5)
# nx.write_pajek(G2,'song_matrix.net')






