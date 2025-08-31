"""

Create the following graphs with correspondent labels in the nodes and weights in the edges if needed, and post the results in the discussion:

G(V,E), V = {A,B,C,Z}, E = {{A,C},{C,Z},{B,Z}} 

"""

import networkx as nx

import matplotlib.pyplot as mp


G = nx.Graph()

nodes = ["A","B","C","Z"]

edges = [("A","C"),("C","Z"),("B","Z")]

G.add_nodes_from(nodes)

G.add_edges_from(edges)

nx.draw(G,with_labels=True, font_color="black", node_color="green")

mp.show()