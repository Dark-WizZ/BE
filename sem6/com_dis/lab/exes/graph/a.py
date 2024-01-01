import graphviz

def draw():
    
  graph = graphviz.Digraph(format='png',graph_attr={'rankdir': 'LR'})

  nodes = [
    (1,2,'a')
  ]
  for (s, d, l) in nodes:
    graph.edge(str(s),str(d),label=l)

  return graph

graph = draw()
graph.view()
