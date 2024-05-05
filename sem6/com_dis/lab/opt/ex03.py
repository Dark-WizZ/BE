e=u'\u03b5'
p=[]

class Prod:
  def __init__(self, name, products):
    self.name = name
    self.products = products
    
  def print(self):
    s = f'{self.name} ->'
    for p in self.products:
      s += f' {p} |'
    s=s[:-1]
    print(s)
    
def trans():
  for x in p:
    alpha=[]
    beta=[]
    for prod in x.products:
      if x.name == prod[0]:
        alpha.append(prod[1:])
      else:
        beta.append(prod)
    if alpha:
      for i in range(len(beta)):
        beta[i]=f'{beta[i]}{x.name}`'
      for i in range(len(alpha)):
        alpha[i]=f'{alpha[i]}{x.name}`'
      alpha.append(e)
      x.products=beta
      p.append(Prod(f'{x.name}`',alpha))
      
n=int(input("No. productions: "))
# inp = ['E -> E+T | T','T -> T*F | F','F -> (E) | id']
for i in range(n):
  name, prods = input(f'Enter prodution {1+1}: ').split(' -> ')
  prods = prods.split(' | ')
  p.append(Prod(name, prods))
  
print('productions: ')
for x in p : x.print()
print('tranforming...')
trans()
for x in p : x.print()