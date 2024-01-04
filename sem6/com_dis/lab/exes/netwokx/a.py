import networkx as nx
import matplotlib.pyplot as plt

graph = nx.DiGraph()

graph.add_edge('q0','qf')
pos = nx.spring_layout(graph)
nx.draw(graph)
nx.draw_networkx_edge_labels(graph, pos=pos,edge_labels='a')

plt.show()