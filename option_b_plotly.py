import pandas as pd
import networkx as nx
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("cartel_network_timeline.csv")

# Create graph
G = nx.from_pandas_edgelist(df, source="source", target="target", edge_attr=["weight", "type"])

# Centrality scores
degree = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G, weight="weight")

# Node layout
pos = nx.spring_layout(G, seed=42, k=2.0)

# Initialize lists
node_x, node_y, node_text, node_size, node_color = [], [], [], [], []

# Process each node
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)

    hover_text = (
        f"Name: {node}<br>"
        f"Connections (Degree Centrality): {degree[node]*100:.1f}%<br>"
        f"Influence as a Bridge (Betweenness): {betweenness[node]*100:.1f}%"
    )

    node_text.append(hover_text)
    node_size.append(20 + 40 * degree[node])
    node_color.append(betweenness[node])

# Process edges
edge_x, edge_y = [], []
for u, v in G.edges():
    x0, y0 = pos[u]
    x1, y1 = pos[v]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]

# Edges trace
edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1, color="#888"),
    hoverinfo='none',
    mode='lines'
)

# Nodes trace
node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    textposition="top center",
    text=[node for node in G.nodes()],
    hovertext=node_text,
    hoverinfo="text",
    marker=dict(
        showscale=True,
        colorscale='Reds',
        reversescale=False,
        color=node_color,
        size=node_size,
        colorbar=dict(
            thickness=15,
            title='Betweenness Centrality',
            xanchor='left',
        ),
        line_width=2
    )
)

# Final figure layout
fig = go.Figure(
    data=[edge_trace, node_trace],
    layout=go.Layout(
        title=dict(
            text='Cartel Network - Node Influence (Hover)',
            font=dict(size=20)
        ),
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20, l=20, r=20, t=40),
        annotations=[dict(
            text="Hover for node influence details",
            showarrow=False,
            xref="paper", yref="paper",
            x=0.005, y=-0.002
        )],
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False)
    )
)

fig.show()
