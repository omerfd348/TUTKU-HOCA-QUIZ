import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# GRAPH 1: Distance Graph
# -------------------------

df = pd.read_csv("data.csv")
G = nx.Graph()

for _, row in df.iterrows():
    G.add_edge(row['source'], row['target'], weight=row['distance'])

# Shortest Path
sp_path = nx.shortest_path(G, source="Depot", target="D", weight='weight')
sp_distance = nx.shortest_path_length(G, source="Depot", target="D", weight='weight')

print("=== SHORTEST PATH ===")
print("Path:", sp_path)
print("Distance:", sp_distance)

# Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G, weight='weight')

print("\n=== MINIMUM SPANNING TREE ===")
for edge in mst.edges(data=True):
    print(edge)

# -------------------------
# GRAPH 2: Capacity Graph
# -------------------------

df_cap = pd.read_csv("capacity.csv")
G_cap = nx.DiGraph()

for _, row in df_cap.iterrows():
    G_cap.add_edge(row['source'], row['target'], capacity=row['capacity'])

# Maximum Flow
flow_value, flow_dict = nx.maximum_flow(G_cap, "Depot", "D")

print("\n=== MAXIMUM FLOW ===")
print("Max Flow:", flow_value)
print("Flow Detail:", flow_dict)

# -------------------------
# VISUALIZATION
# -------------------------

pos = nx.spring_layout(G)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Distance Network")

plt.subplot(1,2,2)
nx.draw(mst, pos, with_labels=True, node_color='lightgreen', node_size=2000)
plt.title("Minimum Spanning Tree")

plt.show()