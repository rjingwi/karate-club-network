import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("Karate Club Network")

st.write(
    "This network represents social relationships among 34 members of a "
    "university karate club. Each node represents a club member, and each "
    "edge represents a social connection between two members."
)

st.sidebar.header("Network Options")

layout = st.sidebar.selectbox(
    "Select network layout",
    ["Spring", "Circular"]
)

G = nx.karate_club_graph()

communities = nx.community.greedy_modularity_communities(G)

community_map = {}

for i, community in enumerate(communities):
    for node in community:
        community_map[node] = i

node_sizes = [G.degree(node) * 100 for node in G.nodes()]
node_colors = [community_map[node] for node in G.nodes()]

if layout == "Spring":
    pos = nx.spring_layout(G, seed=42)
else:
    pos = nx.circular_layout(G)

fig, ax = plt.subplots(figsize=(10, 7))

nx.draw_networkx_edges(
    G,
    pos,
    ax=ax,
    alpha=0.5
)

nx.draw_networkx_nodes(
    G,
    pos,
    ax=ax,
    node_size=node_sizes,
    node_color=node_colors,
    cmap="viridis"
)

nx.draw_networkx_labels(
    G,
    pos,
    ax=ax,
    font_size=8
)

ax.set_title(f"Karate Club Network — {layout} Layout")
ax.axis("off")

st.pyplot(fig)

st.subheader("Structural Encodings")

st.write(
    "Node size represents degree, meaning members with more social connections "
    "appear larger. Node color represents the community detected by the "
    "network structure. These encodings help identify highly connected members "
    "and groups of members that are more closely connected to one another."
)

st.subheader("Limitation")

st.write(
    "The visualization can become difficult to read as the number of nodes and "
    "edges increases. Overlapping edges may obscure individual relationships, "
    "and community detection represents an algorithmic grouping rather than "
    "necessarily a real-world social group."
)
