e = u'\u03b5'
p=[]

class Prod:
  def __init__(self, name, products):
    self.name = name
    self.products = products
  def print(self):
    s = f'{self.name} ->'
    for p in self.products:
      s += f' {p} |'
    s = s[:-1]
    print(s)
    
def trans():
  a = p[0]
  temp = a.products
  a.products=[]
  temp.sort
  while(temp):
    group=[]; alpha=''; beta=[]
    for i in range(1,len(temp)):
      if temp[0][0] == temp[i][0]:
        group.append(temp[i])
    if group:
      group.insert(0, temp[0])
      temp = [j for j in temp if j not in group]
      for j in range(len(group)):
        group[j]+=e
      for c in group[0]:
        for j in group:
          if c != j[0]:
            beta = group
            break
        else:
          alpha+=group[0][0]
          for j in range(len(group)):
            group[j]=group[j][1:]
      for j in range(len(beta)):
        if beta[j]!=e:
          beta[j]=beta[j][:-1]
      a.products.append(f'{alpha}{alpha[0]}`')
      p.append(Prod(f'{alpha[0]}`',beta))
    else:
      a.products.append(temp[0])
      temp.pop(0)
      
input = "A -> ABs | AB | Sed | Swa | f"
name, prods = input.split(' -> ')
prods = prods.split(' | ')
p.append(Prod(name, prods))

print("Productions: ")
for x in p : x.print()
print("Transforming...")
trans()
for x in p: x.print()