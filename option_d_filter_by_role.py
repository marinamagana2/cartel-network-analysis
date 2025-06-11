import pandas as pd
import networkx as nx
import plotly.graph_objects as go

# Load the CSV
df = pd.read_csv("cartel_network_timeline.csv")

# Friendly labels mapping
type_labels = {
    "leader": "Leadership Links",
    "alliance": "Alliances",
    "conflict": "Conflicts",
    "subcell": "Subcell Ties",
    "command": "Command Chains",
    "bribe": "Bribery Routes"
}

# Unique edge types from the data
unique_types = df['type'].unique()

# Full graph layout for consistency
G_all = nx.from_pandas_edgelist(df, source="source", target="target", edge_attr=["weight", "type"])
pos = nx.spring_layout(G_all, seed=42, k=2.0)

# Create frames for each role filter
frames = []
for t in unique_types:
    df_filtered = df[df['type'] == t]
    G = nx.from_pandas_edgelist(df_filtered, source="source", target="target", edge_attr=True)

    degree = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G, weight="weight")

    node_x, node_y, node_text, node_size, node_color = [], [], [], [], []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        hover = f"<b>{node}</b><br>Connections: {degree.get(node, 0):.2f}<br>Influence Score: {betweenness.get(node, 0):.2f}"
        node_text.append(hover)
        node_size.append(20 + 40 * degree.get(node, 0))
        node_color.append(betweenness.get(node, 0))

    edge_x, edge_y = [], []
    for u, v in G.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color="gray"),
        hoverinfo="text",
        mode="lines",
        text=[f"Type of Connection: {type_labels.get(t, t)}"] * len(G.edges())
    )

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode="markers+text",
        text=[node for node in G.nodes()],
        textposition="top center",
        hovertext=node_text,
        hoverinfo="text",
        marker=dict(
            showscale=True,
            colorscale='Reds',
            color=node_color,
            size=node_size,
            colorbar=dict(
                thickness=15,
                title='Influence Score',
                xanchor='left'
            ),
            line_width=2
        )
    )

    frames.append(go.Frame(data=[edge_trace, node_trace], name=t))

# Start with the last frame as default
initial_data = frames[-1].data

# Create dropdown with user-friendly names
buttons = [
    dict(
        label=f"Show Only: {type_labels.get(t, t.title())}",
        method="animate",
        args=[[t], {"frame": {"duration": 0, "redraw": True}}]
    ) for t in unique_types
]

# Final figure setup
fig = go.Figure(
    data=initial_data,
    layout=go.Layout(
        title="Cartel Network - Filter by Relationship Type",
        showlegend=False,
        hovermode="closest",
        updatemenus=[dict(
            type="dropdown",
            direction="down",
            showactive=True,
            buttons=buttons,
            x=0.1,
            xanchor="left",
            y=1.15,
            yanchor="top"
        )],
        margin=dict(b=20, l=20, r=20, t=60),
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False)
    ),
    frames=frames
)

fig.show()
