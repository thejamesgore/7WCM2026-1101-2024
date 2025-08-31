import networkx as nx
# import matplotlib.pyplot as plt

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

# plt.title("Graph Representation of Cities and Distances")
# plt.show()

def tsp_bf(graph, verbose = False):
    # break this down into the smallest problems possible and solve them each
    
    # 1. you need to be able to traverse each node on the graph
    # # can be done by printing each node
    
    # 2. need to be able to list each potential path with the nodes
    ## can print these out too
    
    # 3. need to consider the weights next when doing this so can track the total distance
    # 4. then store the weights somewhere
    # 5. then compare the current distance to the last distance and see if it's more or less
    # 6. if it's less then that's the new best path
    
    
    
tsp_bf(graph)