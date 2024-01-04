import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
graph = nx.DiGraph()

# Add nodes
graph.add_nodes_from(["A", "B"])

# Add edges with different labels
graph.add_edge("A", "B", label="Label1")
graph.add_edge("B", "A", label="Label2")

# Draw the graph using pygraphviz layout for better handling of multiple edges
pos = nx.nx_agraph.graphviz_layout(graph, prog="dot")
labels = nx.get_edge_attributes(graph, 'label')
nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, connectionstyle='arc3,rad=0.1')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

plt.show()
