import networkx as nx

import matplotlib.pyplot as mp

 

#undirected graph

 

G = nx.MultiGraph()

 

nodes=["A","B"]

 

G.add_nodes_from(nodes)



G.add_edge("A","B", weight=1)

G.add_edge("A","B", weight=3)

# Nodes

pos= nx.circular_layout(G)



nx.draw_networkx_nodes(G,pos)

 

# Edges

nx.draw_networkx_edges(G, pos)

 

# Node labels

nx.draw_networkx_labels(G, pos)

mp.show()