# Emergency Response Network using Graph Theory
# Full Working Python Project

# Required Libraries:
# pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt

# -----------------------------------
# CREATE GRAPH
# -----------------------------------

G = nx.Graph()

# -----------------------------------
# ADD NODES
# -----------------------------------

locations = [
    "Hospital",
    "FireStation",
    "PoliceStation",
    "Junction1",
    "Junction2",
    "Emergency"
]

G.add_nodes_from(locations)

# -----------------------------------
# ADD EDGES WITH DISTANCES
# (Source, Destination, Weight)
# -----------------------------------

roads = [
    ("Hospital", "Junction1", 4),
    ("FireStation", "Junction1", 2),
    ("PoliceStation", "Junction2", 3),
    ("Junction1", "Junction2", 2),
    ("Junction1", "Emergency", 5),
    ("Junction2", "Emergency", 4)
]

G.add_weighted_edges_from(roads)

# -----------------------------------
# DISPLAY ALL LOCATIONS
# -----------------------------------

print("\n===== EMERGENCY RESPONSE NETWORK =====\n")

print("Available Locations:")
for node in G.nodes():
    print("-", node)

# -----------------------------------
# USER INPUT
# -----------------------------------

source = input("\nEnter Source Location: ")
destination = input("Enter Emergency Location: ")

# -----------------------------------
# CHECK VALID INPUT
# -----------------------------------

if source not in G.nodes():
    print("\nInvalid Source Location!")
    exit()

if destination not in G.nodes():
    print("\nInvalid Destination Location!")
    exit()

# -----------------------------------
# FIND SHORTEST PATH
# USING DIJKSTRA ALGORITHM
# -----------------------------------

try:
    shortest_path = nx.shortest_path(
        G,
        source=source,
        target=destination,
        weight='weight'
    )

    shortest_distance = nx.shortest_path_length(
        G,
        source=source,
        target=destination,
        weight='weight'
    )

    # -----------------------------------
    # DISPLAY RESULTS
    # -----------------------------------

    print("\n===== SHORTEST ROUTE =====")

    print("\nOptimal Path:")
    print(" -> ".join(shortest_path))

    print("\nTotal Distance:", shortest_distance, "km")

except nx.NetworkXNoPath:
    print("\nNo path exists between the locations!")
    exit()

# -----------------------------------
# VISUALIZE GRAPH
# -----------------------------------

plt.figure(figsize=(12, 8))

# Position layout
pos = nx.spring_layout(G, k=1, seed=42)

# Draw nodes
nx.draw_networkx_nodes(
    G,
    pos,
    node_size=3000
)

# Draw edges
nx.draw_networkx_edges(
    G,
    pos,
    width=2
)

# Draw labels
nx.draw_networkx_labels(
    G,
    pos,
    font_size=10,
    font_weight='bold'
)

# Edge labels (weights)
edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=10
)

# Highlight shortest path
path_edges = list(zip(shortest_path, shortest_path[1:]))

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=path_edges,
    edge_color='red',
    width=4
)

plt.title("Emergency Response Network")

plt.axis('off')

plt.show()