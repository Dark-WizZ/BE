import networkx as nx
import matplotlib.pyplot as plt
import re

t = 0                                                                                                 
f = 1


def nodret(ip):
    global t, f
    e = u'\u03b5'
    nodes = []
    if re.match(re.compile(r'^[a-z]$'), ip):
        nodes = [
            (t, t + 1, ip)
        ]
        t += 1
    elif re.match(re.compile(r'^[a-z]\*$'), ip):
        nodes = [
            (t, t + 1, e),
            (t, t + 3, e),
            (t + 1, t + 2, ip[0]),
            (t + 2, t + 1, e),
            (t + 2, t + 3, e)
        ]
        t += 3
    elif re.match(re.compile(r'^[a-z]\/[a-z]$'), ip):
        nodes = [
            (t, t + 1, e),
            (t, t + 3, e),
            (t + 1, t + 2, ip[0]),
            (t + 3, t + 4, ip[2]),
            (t + 2, t + 5, e),
            (t + 4, t + 5, e),
        ]
        t += 5
    else:
        print("please enter basic expressions(combination of a, a*, a/b, a b)")
        f = 0
    return nodes


def draw(ip):
    graph = nx.DiGraph()
    nodes = []
    for ch in ip.split():
        nodes += nodret(ch)

    for (s, d, l) in nodes:
        graph.add_edge(str(s), str(d), label=l)

    pos = nx.spring_layout(graph)  # You can choose a different layout
    labels = nx.get_edge_attributes(graph, 'label')
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.show()


ip = input("enter regex (leave space between each ip): ")
draw(ip)
