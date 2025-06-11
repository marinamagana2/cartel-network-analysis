import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Optional: for improving text overlap (disabled by default)
# from adjustText import adjust_text

# Load dataset
df = pd.read_csv("cartel_network_timeline.csv")

# Create graph with edge attributes
G = nx.from_pandas_edgelist(df, source="source", target="target", edge_attr=["weight", "type"])

# --- Centrality Measures ---
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G, weight="weight")

# Debug Stats
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("\nTop 5 by Degree Centrality:")
for node, score in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{node}: {score:.3f}")
print("\nTop 5 by Betweenness Centrality:")
for node, score in sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{node}: {score:.3f}")

# --- Visualization Settings ---
node_sizes = [6000 * degree_centrality[node] + 100 for node in G.nodes()]
node_colors = [betweenness_centrality[node] for node in G.nodes()]
edge_weights = [G[u][v]["weight"] * 0.5 for u, v in G.edges()]

# Spring layout with spacing
pos = nx.spring_layout(G, seed=42, k=2.0)

# Plot
fig, ax = plt.subplots(figsize=(14, 10))  # Scaled smaller for better fit

# Draw nodes and edges
nodes = nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors, node_size=node_sizes, cmap=plt.cm.Reds)
nx.draw_networkx_edges(G, pos, ax=ax, edge_color="gray", width=edge_weights)

# Label nodes (simplified — all shown)
nx.draw_networkx_labels(G, pos, ax=ax, font_size=7)

# Optional advanced label adjustment (disabled unless needed)
# texts = [plt.text(x, y, s, fontsize=7) for s, (x, y) in pos.items()]
# adjust_text(texts)

# Colorbar
sm = plt.cm.ScalarMappable(cmap=plt.cm.Reds)
sm.set_array(node_colors)
plt.colorbar(sm, ax=ax, label="Betweenness Centrality")

# Title and axis cleanup
ax.set_title("Cartel Network - Node Influence", fontsize=14)
ax.set_axis_off()
plt.subplots_adjust(left=0.05, right=0.9, top=0.92, bottom=0.08)  # ensure nothing cuts off
plt.show()
