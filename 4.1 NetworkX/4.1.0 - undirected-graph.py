import networkx as nx

import matplotlib.pyplot as mp

#undirected graph

G = nx.Graph()

G.add_node(1)

G.add_node(2)

G.add_edge(1,2)

nx.draw(G,with_labels=True, font_color="white")

mp.show()