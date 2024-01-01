import graphviz

def draw():
    
  graph = graphviz.Digraph(format='png',graph_attr={'rankdir': 'LR'})

  nodes = [
    (1,2,'e'),
    (1,4,'e'),
    (2,3,'a'),
    (4,5,'b'),
    (3,6,'e'),
    (5,6,'e'),
  ]
  for (s, d, l) in nodes:
    graph.edge(str(s),str(d),label=l)

  return graph

graph = draw()
graph.view()
