import pandas as pd
import networkx as nx
import plotly.graph_objects as go

# Load the CSV with timeline info
df = pd.read_csv("cartel_network_timeline.csv")

# Prepare list to store frames
frames = []

# Loop over each year to create subgraphs
for year in sorted(df['year'].unique()):
    df_year = df[df['year'] <= year]

    G = nx.from_pandas_edgelist(df_year, source="source", target="target", edge_attr=["weight", "type"])

    degree = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G, weight="weight")
    pos = nx.spring_layout(G, seed=42, k=2.0)

    node_x, node_y, node_text, node_size, node_color = [], [], [], [], []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

        hover_text = f"{node}<br>Influence Score: {betweenness[node]:.2f}<br>Connections: {degree[node]:.2f}"
        node_text.append(hover_text)

        node_size.append(20 + 40 * degree[node])
        node_color.append(betweenness[node])

    edge_x, edge_y = [], []
    for u, v in G.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color="#888"),
        hoverinfo='none',
        mode='lines'
    )

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
            color=node_color,
            size=node_size,
            colorbar=dict(
                thickness=15,
                title='Influence (Betweenness)',
                xanchor='left',
            ),
            line_width=2
        )
    )

    frames.append(go.Frame(data=[edge_trace, node_trace], name=str(year)))

# Use the latest year for initial figure
initial_data = frames[-1].data

# Create animation figure
fig = go.Figure(
    data=initial_data,
    layout=go.Layout(
        title='Cartel Network Over Time',
        showlegend=False,
        hovermode='closest', 
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[dict(label="Play", method="animate", args=[None])]
        )],
        margin=dict(b=20, l=20, r=20, t=40),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False)

    ),
    frames=frames
)

fig.show()
