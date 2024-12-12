import networkx as nx

import matplotlib.pyplot as mp

 

#another undirected graph

 

G = nx.Graph()

 

nodes=["A","B","C","D","E"]

 

G.add_nodes_from(nodes)

 

list_of_edges=[("A","E")]

 

G.add_edges_from(list_of_edges)

 

nx.draw(G,with_labels=True)

mp.show()