import graphviz

def draw():
    
  graph = graphviz.Digraph(format='png',graph_attr={'rankdir': 'LR'})

  nodes = [
    (1,2,'e'),
    (1,4,'e'),
    (2,3,'a'),
    (3,2,'e'),
    (3,4,'e')
  ]
  for (s, d, l) in nodes:
    graph.edge(str(s),str(d),label=l)

  return graph

graph = draw()
graph.view()
