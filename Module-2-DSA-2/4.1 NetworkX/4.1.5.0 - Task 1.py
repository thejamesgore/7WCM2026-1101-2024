"""

Create the following graphs with correspondent labels in the nodes and weights in the edges if needed, and post the results in the discussion:

G(V,E), V = {a,b,c,d,}, E = {(a,b),(b,c),(c,d),(d,a)} 

"""

import networkx as nx

import matplotlib.pyplot as mp

G = nx.DiGraph()

nodes = ["A","B","C","D"]

edges = [("A","B"),("B","C"),("C","D"),("D","A")]

G.add_nodes_from(nodes)

G.add_edges_from(edges)

nx.draw(G,with_labels=True)

mp.show()