import networkx as nx
import matplotlib.pyplot as mp

G = nx.DiGraph()

nodes = ["A", "B", "C"]
edges = [("A", "C"), ("A", "B"), ("C", "B"), ("B", "A"), ("B", "C")]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Get positions for nodes
pos = nx.spring_layout(G)

# Draw edges with styles directly
nx.draw_networkx_edges(G, pos, edgelist=[("A", "C"), ("A", "B")], style="dashed", edge_color="black", arrows=True, arrowsize=20)
nx.draw_networkx_edges(G, pos, edgelist=[("C", "B")], style="dotted", edge_color="black", arrows=True, arrowsize=20)
nx.draw_networkx_edges(G, pos, edgelist=[("B", "A"), ("B", "C")], style="solid", edge_color="black", arrows=True, arrowsize=20)

# Draw nodes and labels
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_color="black")

mp.title("Directed Graph with Styled Edges", fontsize=16)
mp.show()
