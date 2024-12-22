import networkx as nx
import matplotlib.pyplot as mp
from depth_first_search import depth_first_search as dfs

nodes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]  # List of nodes
edges = [("1", "2"), ("1", "3"), ("1", "4"),       # Node 1 is root
         ("2", "5"), ("2", "6"),               # Branch from node 2
         ("3", "7"), ("3", "8"),               # Branch from node 3
         ("4", "9"), ("4", "10"),              # Branch from node 4
         ("5", "11"), ("5", "12"),             # Branch from node 5
         ("6", "13"), ("6", "14"),             # Branch from node 6
         ("7", "15"), ("7", "16"),             # Branch from node 7
         ("8", "17"), ("8", "18"),             # Branch from node 8
         ("9", "19"), ("9", "20"),             # Branch from node 9
         ("10", "21"), ("10", "22")]           # Branch from node 10

G = nx.DiGraph()
G.add_nodes_from(nodes)  
G.add_edges_from(edges) 


pos = nx.spring_layout(G, seed=42)  
nx.draw(G, pos, with_labels=True, node_color="green", node_size=700, font_size=10, arrows=True)
mp.show()

dfs(G, "19", "1", verbose=True)