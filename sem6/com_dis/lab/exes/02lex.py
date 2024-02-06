import re

e = u'\u03b5'
t=0

ip = 'a a* ( a ( i / p ) s a ) o / p'

class NFA():
    def __init__(self, s, ip):
        self.s=s
        self.ip = ip
        self.paths = [(s, s+1, ip)]

ips = ip.split()

for i in range(len(ips)):
    if (re.match('[a-z]',ips[i])):
        ips[i] = NFA(0,ips[i][0])

for x in ips:
    if isinstance(x, NFA):
        print(x.paths)
    else:
        print(x)


def simplify(ips):
    s=0; e=0; f=0
    for i in range(len(ips)):
        if(ips[i]=='(' and not f):
           f=1
           s=i+1
        if(ips[i]==')':
           e=i-1
           break

           
