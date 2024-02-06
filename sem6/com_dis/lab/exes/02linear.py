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
        s = nfa.s
        f = nfa.f
        p = [(0,s,e),(0,f+1,e)]
        p += nfa.paths
        p += [(f,s,e),(f,f+1,e)]
        self.paths = p
        self.f = nfa.f+1

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
        nfa.s = 0
        nfa.f = f2+1
        return nfa

    def __add__(self, o):
        nfa1 = copy.deepcopy(self)
        nfa2 = o.rearrange(self.f)
        nfa1.paths += nfa2.paths
        nfa1.f=nfa2.f
        return nfa1

    def rearrange(self, s):
        temp = copy.deepcopy(self)
        for u, v, w in temp.paths:
            temp.paths[temp.paths.index((u,v,w))]=(u+s,v+s,w)
        temp.s += s
        temp.f += s
        return temp

    def print(self):
        print('start: ',self.s,'end: ',self.f)
        print(self.paths)

ip = input('enter...')
ips = ip.split()

pros=[]
for i in ips:
    if re.match(re.compile(r'^[a-z]$'), i):
        pros.append(NFA(0,i))
    elif re.match(re.compile(r'^[a-z]\*$'), i):
        nfa = NFA(0,i[0])
        nfa.star()
        pros.append(nfa)
    else:
        pros.append(i)

print('pros debug..')
for x in pros:
    if isinstance(x, NFA):
        x.print()
    else:
        print(x)

ors=[]

while(len(pros) > 1):
    if(isinstance(pros[0],NFA) and isinstance(pros[1],NFA)):
        temp = pros[0] + pros[1]
        pros.pop(0); pros.pop(0)
        pros.insert(0, temp)

    else:
        ors += pros[:1]

        pros.pop(0)
        if pros:
            pros.pop(0)

ors+=pros

print('ors debug.. ')
for x in ors:
    if isinstance(x, NFA):
        x.print()
    else:
        print(x)

while(len(ors)>1):
    temp = ors[0] | ors[1]
    ors.pop(0); ors.pop(0)
    ors.insert(0, temp)

print('ors debg..')

for x in ors:
    if isinstance(x, NFA):
        x.print()
    else:
        print(x)

graph = graphviz.Digraph(format='png',graph_attr={'rankdir': 'LR'})
for (s,d,l) in ors[0].paths:
    graph.edge(str(s), str(d), label=l)

graph.view()

# print('sandboxing..')
#
# a = NFA(0,'')
# print('a: ')
# print(a.s, a.f)
# b = NFA(0,'')
# print('b: ')
# print(b.s,b.f)


# a.paths = [(0, 1, 'a'), (1, 2, 'ε'), (1, 4, 'ε'), (2, 3, 'b'), (3, 2, 'ε'), (3, 4, 'ε')]
# a.s = 0
# a.f = 4
# b.paths = [(0, 1, 'b'), (1, 2, 'j')]
# b.s=0
# b.f=2
# c=a|b
#
# print(c.paths)
