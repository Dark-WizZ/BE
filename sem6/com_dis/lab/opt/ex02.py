import re

t=0; f=1

def gen_nodes(ip):
  global t, f
  e=u'\u03b5'
  nodes = []
  
  if re.match(re.compile(r'^[a-z]$'),ip):
    nodes = [(t,t+1,ip)]
    t+=1
  elif re.match(re.compile(r'^[a-z]\*$'),ip):
    nodes = [
      (t, t+1, e), (t+1,t+2,ip[0]),
      (t+2, t+3, e), (t,t+3,e),
      (t+2, t+1, e)
    ]
    t+=3
  elif re.match(re.compile(r'^[a-z]\/[a-z]$'),ip):
    nodes = [
      (t,t+1, e), (t+1, t+2, ip[0]),
      (t,t+3,e), (t+3, t+4, ip[2]),
      (t+2, t+5, e), (t+4, t+5, e)
    ]
    t+=5
  else:
    print("please enter basic expressions (linear combination of a a* a/b)")
    f=0
  return nodes

def gen_tab(nodes):
  ips = list(set([i for s, d, i in nodes]))
  ips.sort()
  
  a = [[[] for j in ips] for i in range(t)]
  
  for s, d, i in nodes:
    a[s][ips.index(i)].append(d)
  print('state', end='')
  for x in ips:
    print(f'\t{x}', end='')
  print('\n','-'*20)
  
  for i in range(t):
    print(i, end='')
    for j in range(len(ips)):
      print(f'\t{a[i][j]}',end='')
    print()
  print(f'state {t} is the final state.')

ip = input("Enter regex: ")

nodes = []

for i in ip.split():
  nodes += gen_nodes(i)
if f:
  gen_tab(nodes)