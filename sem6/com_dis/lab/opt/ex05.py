import re
p=[]
class Prod:
  def __init__(self, name, products):
    self.name=name
    self.products=products
    self.first=[]
    self.follow=[]

def find_prod(name):
  for x in p:
    if x.name == name: return x

def is_terminal(s):
  return not re.match(re.compile('^[A-Z]$'),s)

def calc_first():
  for x in reversed(p):
    for pr in x.products:
      for c in range(len(pr)):
        if is_terminal(pr[c]):
          x.first.append(pr[c])
          break
        else:
          f = find_prod(pr[c]).first
          x.first += f
          if('e' not in f):
            break
    x.first = list(set(x.first))

def calc_follow():
  p[0].follow.append('$')
  for x in p:
    find_follow(x)
    
def find_follow(x):
  for y in p:
    for pr in y.products:
      for c in range(len(pr)):
        if pr[c] == x.name:
          if c+1 == len(pr):
            x.follow += y.follow
          elif is_terminal(pr[c+1]):
            x.follow.append(pr[c+1])
          else:
            next = find_prod(pr[c+1])
            if 'e' not in next.first:
              x.follow += next.first
            elif next.follow:
              x.follow += next.first + next.follow
            else:
              x.follow += next.first + find_follow(next)
            
  x.follow = list(set(x.follow)- {'e'})
  return x.follow
  
sample=['E -> TX', 'X -> +TX | e','T -> FY','Y -> *FY | e','F -> (E) | i']
# sample=['S -> aBDh', 'B -> cC','C -> bC | e','D -> EF','E -> g | e','F -> f | e']
for ip in sample:
  name, products = ip.split(' -> ')
  products = products.split(" | ")
  p.append(Prod(name, products))

calc_first()
calc_follow()

#print first
for x in p: print(f'first({x.name}) = {x.first}')
for x in p: print(f'follow({x.name}) = {x.follow}')