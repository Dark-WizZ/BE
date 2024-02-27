import re

p=[]
class Prod:
    def __init__(self, name, products):
        self.name=name
        self.products=products
        self.first=[]
        self.follow=[]
      
    def print(self):
        s = f'{self.name} -> '
        for p in self.products:
            s+= f' {p} |'
        s=s.rstrip('|')
        print(s)    

def is_terminal(s):
    if re.match(re.compile('^[A-Z]$'),s):
        return False
    else:
        return True

#find production by name:
def find_prod(name):
    for x in p:
        if x.name == name:
            return x

#find first
def calc_first():
    for i in reversed(range(len(p))):
        for x in p[i].products:
            if is_terminal(x[0]):
                p[i].first.append(x[0])
            else:
                f = find_prod(x[0]).first
                p[i].first.extend(f)
                c=1
                while 'e' in f:
                    f=find_prod(x[c]).first
                    p[i].first.extend(f)
                    c+=1
                    if c == len(x): break
                

n = int(input("No of production: "))
for i in range(n):
      ip = input(f"Production {i+1}: ")
      name, prods = ip.split(' -> ')
      products = prods.split(' | ')
      p.append(Prod(name, products))
  
print('Productions:')
for x in p: x.print()

calc_first()

#print first and follow
for x in p: print(f'first({x.name}) = {x.first}')
for x in p: print(f'follow({x.name}) = {x.follow}')
