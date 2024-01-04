import graphviz
import re

t=0; f=1

def nodret(ip):
  global t, f
  e = u'\u03b5'
  nodes=[]
  if re.match(re.compile(r'^[a-z]$'), ip):
    nodes = [
      (t,t+1,ip)
    ]
    t+=1
  elif re.match(re.compile(r'^[a-z]\*$'), ip):
    nodes = [
      (t,t+1,e),
      (t,t+3,e),
      (t+1,t+2,ip[0]),
      (t+2,t+1,e),
      (t+2,t+3,e)
    ]
    t+=3
  elif re.match(re.compile(r'^[a-z]\/[a-z]$'), ip):
    nodes = [
      (t,t+1,e),
      (t,t+3,e),
      (t+1,t+2,ip[0]),
      (t+3,t+4,ip[2]),
      (t+2,t+5,e),
      (t+4,t+5,e),
    ]
    t+=5
  else:
    print("please enter basic expressions(combination of a, a*, a/b, a b)")
    f=0
  return nodes

def draw(ip):
    
  graph = graphviz.Digraph(format='png',graph_attr={'rankdir': 'LR'})
  nodes=[]
  for ch in ip.split():
    nodes += nodret(ch)
  for (s, d, l) in nodes:
    graph.edge(str(s),str(d),label=l)

  return graph

ip = input("enter regex(leave space between each ip): ")
graph = draw(ip)

if f:
  graph.view()
