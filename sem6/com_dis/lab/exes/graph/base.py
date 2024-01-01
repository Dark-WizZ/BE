import graphviz
import re

def draw(ip):
    
  graph = graphviz.Digraph(format='png',graph_attr={'rankdir': 'LR'})

  if re.match(re.compile(r'^[a-z]$'), ip):
    nodes = [
      (1,2,ip)
    ]
  elif re.match(re.compile(r'^[a-z]\*$'), ip):
    nodes = [
      (1,2,'e'),
      (1,4,'e'),
      (2,3,ip[0]),
      (3,2,'e'),
      (3,4,'e')
    ]
  elif re.match(re.compile(r'^[a-z][a-z]$'), ip):
    nodes = [
      (1,2,ip[0]),
      (2,3,ip[1])
    ]
  elif re.match(re.compile(r'^[a-z]\/[a-z]$'), ip):
    nodes = [
      (1,2,'e'),
      (1,4,'e'),
      (2,3,ip[0]),
      (4,5,ip[2]),
      (3,6,'e'),
      (5,6,'e'),
    ]
  for (s, d, l) in nodes:
    graph.edge(str(s),str(d),label=l)

  return graph

ip = input("enter regex: ")
graph = draw(ip)
graph.view()
