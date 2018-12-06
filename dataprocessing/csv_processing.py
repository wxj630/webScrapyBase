import numpy as np
import pandas as pd
import networkx as nx

csv_file = pd.read_csv('final_matrix2.csv')
df = pd.DataFrame(csv_file)
df2=df.fillna(0)
df3=df2.T




df3.to_excel('final_matrix2.xlsx')

# nx.write_pajek(df,'pajek.net')




