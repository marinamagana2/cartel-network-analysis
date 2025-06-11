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

I’ve always been curious about how criminal networks actually work — not just what they do, but how they’re structured behind the scenes. This project came from that curiosity, shaped a bit by what I’ve grown up around and what I might want to do in the future.

I used Python, NetworkX, Plotly, and real-world cartel data to build visualizations of groups like CJNG, Sinaloa, La Familia Michoacana, and others. The graphs show who’s connected to who, how strong those ties are, and how power moves through the network whether through alliances, leadership, or even conflict.

Even though these groups aren’t always centralized, it becomes pretty clear that a few key players control a lot behind the scenes. Mapping that out helped me see how useful this kind of analysis could be — especially for people working in public safety or intelligence. It's the kind of thing I could actually see myself doing one day.

