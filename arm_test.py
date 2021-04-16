import numpy as np
import pandas as pd
import re
import networkx as nx
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
from apyori import apriori
import random

'''
datass=[]
data=[]
def getRand():
	return random.choice(data)

for i in range(0, 10):
	datas=[]
	for j in range(0, 10):
		rnd=random.choice(data)
		while(rnd in datas):
			rnd=getRand()
		datas.append(rnd)
	datass.append(datas)
print(datass)
'''

result=(list(apriori(dataset, min_support=0.1)))
df=pd.DataFrame(result)
df['length']=df['items'].apply(lambda x:len(x))
df=df[(df['length']==2) & (df['support'] >=0.9)]

G=nx.Graph()
ar=(df['items'])
G.add_edges_from(ar)

pr=nx.pagerank(G)
nsize=np.array([v for v in pr.values()])
nsize=2000*(nsize-min(nsize))/(max(nsize)-min(nsize))
pos=nx.fruchterman_reingold_layout(G)

plt.figure(figsize=(16, 12))
plt.axis('off')
plt.title('association between lecture\n\n', fontsize=20)
plt.xlabel
nx.draw_networkx(G, 
	font_size=100, pos=pos, node_color=list(pr.values()),
	node_size=nsize, alpha=0.7, edge_color='.5',
	cmap=plt.cm.YlGn)

plt.show()
#plt.savefig('fig9.png', dpi=300)