import networkx as nx

import matplotlib.pyplot as mp

 

#undirected weighted graph

 

G = nx.Graph()

 

nodes=["A","B","C","D","E"]

 

G.add_nodes_from(nodes)

 

G.add_edge("A","E", weight=8)

G.add_edge("B","B")

G.add_edge("C","D", weight=15)

 

#Layout set to circular

pos= nx.circular_layout(G)

 

# Nodes

nx.draw_networkx_nodes(G,pos)

 

# Edges

nx.draw_networkx_edges(G, pos)

 

# Node labels

nx.draw_networkx_labels(G, pos)

 

# Edge labels

edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edge_labels(G, pos, edge_labels)

 

mp.show()