t=0
ip='a/b'
v=[
      (t,t+1,'e'),
      (t,t+3,'e'),
      (t+1,t+2,'a'),
      (t+3,t+4,'b'),
      (t+2,t+5,'e'),
      (t+4,t+5,'e'),(5, 6, 'c')  
    ]
t+=6
ips = list(set([e for e1, e2, e in v]))
ips.sort()
print(ips)
'''a = [
    [[1,3],[],[]],
    [[],[2],[]],
    [[5],[],[]],
    [[],[],[4]],
    [[5],[],[]]
]
'''
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
