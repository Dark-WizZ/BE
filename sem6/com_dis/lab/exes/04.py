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
    #for x in p:
        x = p[0]
        temp = x.products
        temp.sort()
        x.prdoucts=[]
        for i in range(len(temp)):
            temp[i] = f'{temp[i]}{e}'
        while temp:
            group=[]
            alpha=''
            beta=[]
            for i in range(1,len(temp)):
                if (temp[0][0] == temp[i][0]):
                    group.append(temp[i])
            if group:
                group.insert(0,temp[0])
                temp = [y for y in temp if y not in group]
                f1=0
                for c in group[0]:
                    for j in range(1, len(group)):
                        if(group[j][0] != c):
                            f1=1
                    if f1:
                        p.append(Prod(f"{alpha[0]}'",group))
                    else:
                        alpha += c
                        for j in range(1, len(group)):
                            group[j] = group[j][1:]

            else:
                x.products.append(temp[0])
                temp.pop(0) 

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
