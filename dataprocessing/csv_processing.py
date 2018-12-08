import numpy as np
import pandas as pd
import networkx as nx
# import matplotlib as plt


csv_file = pd.read_csv('final_matrix2.csv')
df = pd.DataFrame(csv_file)
df2=df.fillna(0)
df3=df2.T

df4=np.dot(df2,df3)
print(df4)



# G1=nx.from_pandas_adjacency(df3)
# nx.write_pajek(G1,'usr2song_matrix.net')
# df3.to_excel('final_matrix2.xlsx')

G = nx.from_pandas_adjacency(df3)
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
# plt.show()




