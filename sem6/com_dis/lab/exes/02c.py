import re

e = u'\u03b5'
t=0

class NFA():
    global t,e
    def __init__(self, start):
        self.start=start

    def gen_single(self, ip):
        global t,e
        self.ip = ip
        s=self.start
        self.paths = [(s,s+1,self.ip)]
        t=self.end=s+1

    def gen_star(self, ip):
        global t,e
        self.ip=ip[0]
        s=self.start
        self.paths=[
                    (s,s+1,e),(s,s+3,e),
                    (s+1,s+2,self.ip),
                    (s+2,s+1,e),(s+2,s+3,e)
                 ]
        t=self.end=s+3

    def gen_or(self, a, b):
        global t,e
        s=self.start
        self.paths = [(s,s+1,e)]

        if re.match(re.compile(r'^[a-z]$'), a):
            a_nfa = NFA(s+1)
            a_nfa.gen_single(a)
        elif re.match(re.compile(r'^[a-z]\*$'), a):
            a_nfa = NFA(s+1)
            a_nfa.gen_star(a)
        
        self.paths += a_nfa.paths + [(s,a_nfa.end+1,e)]
        
        if re.match(re.compile(r'^[a-z]$'), b):
            b_nfa = NFA(a_nfa.end+1)
            b_nfa.gen_single(b)
        elif re.match(re.compile(r'^[a-z]\*$'), b):
            b_nfa = NFA(a_nfa.end+1)
            b_nfa.gen_star(b)
        
        f = b_nfa.end+1
        self.paths += b_nfa.paths + [(a_nfa.end, f, e),(b_nfa.end, f, e)]

        t = self.end=f

    def gen_concat(self, a, b):
        global t,e
        s=self.start
        a_nfa = NFA(s)

        if re.match(re.compile(r'^[a-z]$'), a):
            a_nfa.gen_single(a)
        elif re.match(re.compile(r'^[a-z]\*$'), a):
            a_nfa.gen_star(a)

        b_nfa = NFA(a_nfa.end)

        if re.match(re.compile(r'^[a-z]$'), b):
            b_nfa.gen_single(b)
        elif re.match(re.compile(r'^[a-z]\*$'), b):
            b_nfa.gen_star(b)

        self.paths = a_nfa.paths + b_nfa.paths
        t = self.end = b_nfa.end

def create_nfa(ip):
    nfa = NFA(0)
    if re.match(re.compile(r'^[a-z]$'), ip):
        nfa.gen_single(ip)
    elif re.match(re.compile(r'^[a-z]\*$'), ip):
        nfa.gen_star(ip)
    elif re.match(re.compile(r'^[a-z]\*? \/ [a-z]\*?$'), ip):
        x = ip.split() 
        a=x[0]; b=x[2]
        nfa.gen_or(a,b)
    return nfa.paths

def tab_gen(v):
    ips = list(set([e for e1, e2, e in v]))
    ips.sort()

    a=[[[] for j in range(len(ips))] for i in range(t)]
    for s, d, i in v:
        a[s][ips.index(i)].append(d)
    print('state',end="")
    for x in ips:
        print(f'\t{x}',end='')

    print('\n','-'*(len(ips)*10))
    for i in range(t):
        print(f'{i}',end='')
        for j in range(len(ips)):
            print(f'\t{a[i][j]}',end='')
        print()

ip = input('Enter regular expression: ')
v = create_nfa(ip)
print(v)
tab_gen(v)
