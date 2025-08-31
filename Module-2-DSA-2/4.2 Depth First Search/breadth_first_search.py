import networkx as nx

def bfs(graph, start):
    """
    Perform BFS on a graph starting from the given node.

    Parameters:
    graph (dict): A dictionary representing the adjacency list of the graph.
    Keys are nodes, and values are lists of neighbors.
    start: The starting node for BFS.

    Returns:
    list: A list of nodes in the order they are visited.
    """
    visited = set()  # To track visited nodes
    queue = [start]  # Queue for BFS, initialized with the start node
    traversal_order = []  # To store the order of traversal

    while queue:
        current_node = queue.pop(0)  # Dequeue the front element

        if current_node not in visited:
            visited.add(current_node)  # Mark the node as visited
            traversal_order.append(current_node)  # Add it to the traversal order

            # Enqueue all unvisited neighbors
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

# Generate a random labeled rooted tree using NetworkX
random_tree = nx.random_labeled_rooted_tree(10)
adjacency_list = {node: list(neighbors) for node, neighbors in random_tree.adjacency()}

# Test BFS on the generated tree
start_node = 0  # Assuming nodes are labeled starting from 0
print("Generated Tree (Adjacency List):", adjacency_list)
print("BFS Traversal:", bfs(adjacency_list, start_node))
