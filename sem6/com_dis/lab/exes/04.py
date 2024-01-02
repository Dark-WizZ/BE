
e=u'\u03b5'
p=[]

class Prod:
  def __init__(self, name, products):
    self.name=name
    self.products=products
  
  def print(self):
    s = f'{self.name} -> '
    for p in self.products:
      s+= f' {p} |'
    s=s.rstrip('|')
    print(s)
    
def trans():    
    for x in p:
        temp = x.products
        temp.sort()
        for j in range(len(temp)):
            temp[j]=f'{temp[j]}{e}'
        group=[]
        alpha=[]
        beta=[]
        for j in range(len(temp)-1):
            if(temp[0][:1]==temp[j+1][:1]):
                group.append(temp[j+1])
        for j in group: print('group',j)

n = int(input("No of production: "))
for i in range(n):
    ip = input(f"Production {i+1}: ")
    name, prods = ip.split(' -> ')
    products = prods.split(' | ')
    p.append(Prod(name, products))
  
print('Productions:')
for x in p: x.print()
print('Transforming...')
trans()
for x in p: x.print()
