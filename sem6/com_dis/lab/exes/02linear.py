import re
import copy
import graphviz

e = u'\u03b5'
t=0

class NFA():
    def __init__(self, s, ip):
        self.s = s
        self.paths = [(s, s+1, ip)]
        self.f = s+1

    def star(self):
        nfa = self.rearrange(1)
        s=nfa.s
        f=nfa.f
        p=[(0,s,e),(0,f+1,e)]
        p+=nfa.paths
        p+=[(f,s,e),(f,f+1,e)]
        self.paths=p
        self.f=nfa.f+1

    def __or__(self, o):
        nfa1 = self.rearrange(1)
        nfa2 = o.rearrange(nfa1.f+1)
        s1 = nfa1.s; f1 = nfa1.f
        s2 = nfa2.s; f2 = nfa2.f
        p = [(0,s1, e),(0, s2, e)]
        p += nfa1.paths + nfa2.paths
        p += [(f1, f2+1, e),(f2, f2+1, e)]
        nfa = NFA(0,'')
        nfa.paths = p
        nfa.f = f2+1
        return nfa

    def __add__(self, o):
        nfa1 = copy.deepcopy(self)
        nfa2 = o.rearrange(self.f)
        nfa1.paths += nfa2.paths
        return nfa1

    def rearrange(self, s):
        temp = copy.deepcopy(self)
        for u, v, w in temp.paths:
            temp.paths[temp.paths.index((u,v,w))]=(u+s,v+s,w)
        temp.s += s
        temp.f += s
        return temp

# nfa1 = NFA(0,'a')
# nfa1.star()
# nfa2 = NFA(0,'b')
# nfa2.star()
# nfa=nfa1+nfa2
# nfa=nfa1|nfa2
# nfa += nfa2
# print(nfa.paths)

ip = 'a b* / b j'
ips = ip.split()

pros=[]
for e in ips:
    if re.match(re.compile(r'^[a-z]$'), e):
        pros.append(NFA(0,e))
    elif re.match(re.compile(r'^[a-z]\*$'), e):
        nfa = NFA(0,e[0])
        nfa.star()
        pros.append(nfa)
    else:
        pros.append(e)

for x in pros:
    if isinstance(x, NFA):
        print(x.paths)
    else:
        print(x)

# graph = graphviz.Digraph(format='png',graph_attr={'rankdir': 'LR'})
# for (s,d,l) in nfa.paths:
#     graph.edge(str(s), str(d), label=l)
#
# graph.view()
