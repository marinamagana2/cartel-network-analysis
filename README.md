# 🕵️‍♀️🕸️ Cartel Network Analysis
This project visualizes and analyzes connections within cartel structures using Python. It maps out relationships like leadership, alliances, conflicts, and operational chains to highlight who holds influence, how different actors are linked, and how things evolve over time. 

The network includes groups like CJNG, Sinaloa Cartel, Gulf Cartel, and Los Zetas, with nodes and edges that represent how power and operations flow between figures in places like Jalisco, Tepalcatepec, and Tijuana.

You can see who holds influence (not just leaders, but people who connect key parts of the network), how alliances shift, or how subgroups branch off. There’s even an animation that shows how the network evolves over time — plus a filter option to focus on just leaders, conflicts, or other roles. It’s designed to be informative for analysts, but still easy to understand even if you don’t code.


## 👀 What You Can Do

- **See the full network** at once (static view)
- **Explore interactively** by hovering over nodes (Plotly version)
- **Watch it grow over time** with a timeline animation
- **Filter by role** — like just seeing leaders or conflict ties

## 🧰 Tools Used

- `NetworkX` for graph building and analysis
- `Plotly` and `Matplotlib` for static and interactive visualization
- `Pandas` for handling the data

## 📂 What's Included

- `main.py` — shows the full network graph with influence scores
- `option_b_plotly.py` — interactive graph (you can hover and explore)
- `option_c_animated.py` — animates network growth over time
- `option_d_filter_by_role.py` — lets you filter network by type of connection
- `cartel_network_timeline.csv` — the dataset used

## 💡 Inspiration

This project builds on real-world patterns in criminal networks, with the goal of developing analysis tools relevant to intelligence and security fields.


