import networkx as nx
import matplotlib.pyplot as plt

"""
Solve the traveling salesperson problem with a brute force approach with the following graph
"""

# Define nodes and edges with weights
nodes = ["Paris", "Nantes", "Marseille", "Lyon"]
edges_with_weights = [
    ("Paris", "Nantes", 34),
    ("Paris", "Marseille", 45),
    ("Paris", "Lyon", 33),
    ("Nantes", "Marseille", 41),
    ("Nantes", "Lyon", 29),
    ("Marseille", "Lyon", 15)
]

# Create the graph
graph = nx.Graph()
graph.add_edges_from((u, v, {'weight': w}) for u, v, w in edges_with_weights)

# Visualize the graph
pos = nx.spring_layout(graph)  # Position nodes using spring layout
nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)

# Draw edge labels (weights)
edge_labels = nx.get_edge_attributes(graph, 'weight')  # Get weights as labels
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

plt.title("Graph Representation of Cities and Distances")
plt.show()
