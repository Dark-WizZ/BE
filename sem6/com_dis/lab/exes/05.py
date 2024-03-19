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
                
def calc_follow():
    # Initialize follow sets for all non-terminal symbols
    for prod in p:
        prod.follow = []

    # Add $ to follow(S), where S is the start symbol
    p[0].follow.append('$')

    # Iterate until there are no changes in any follow sets
    while True:
        updated = False
        for prod in p:
            for i, product in enumerate(prod.products):
                for j, symbol in enumerate(product):
                    if is_terminal(symbol):
                        continue

                    if j == len(product) - 1:
                        # If the non-terminal symbol is at the end of the production
                        # Add follow(prod.name) to follow(symbol)
                        for s in prod.follow:
                            if s not in find_prod(symbol).follow:
                                find_prod(symbol).follow.append(s)
                                updated = True
                    else:
                        # If there are symbols after the non-terminal symbol
                        # Add first(symbols after non-terminal symbol) to follow(symbol),
                        # except epsilon ('e')
                        next_symbols = product[j+1:]
                        first_set = []
                        for s in next_symbols:
                            if is_terminal(s):
                                first_set.append(s)
                                break
                            else:
                                first_set.extend(find_prod(s).first)
                                if 'e' not in find_prod(s).first:
                                    break
                        else:
                            # If epsilon ('e') is in all first sets, add follow(prod.name) to follow(symbol)
                            for s in prod.follow:
                                if s not in find_prod(symbol).follow:
                                    find_prod(symbol).follow.append(s)
                                    updated = True
                            continue

                        # Add all symbols in first_set except epsilon ('e') to follow(symbol)
                        for s in first_set:
                            if s != 'e' and s not in find_prod(symbol).follow:
                                find_prod(symbol).follow.append(s)
                                updated = True

        # Break if no changes were made in any follow sets
        if not updated:
            break
# n = int(input("No of production: "))
# for i in range(n):
#       ip = input(f"Production {i+1}: ")
#       name, prods = ip.split(' -> ')
#       products = prods.split(' | ')
#       p.append(Prod(name, products))
  
input = ['S -> aBDh',
         'B -> cC',
         'C -> bC | e',
         'D -> EF',
         'E -> g | e',
         'F -> f | e']
n = 6 
for x in input:
      ip = x
      name, prods = ip.split(' -> ')
      products = prods.split(' | ')
      p.append(Prod(name, products))

print('Productions:')
for x in p: x.print()

calc_first()
calc_follow()

#print first and follow
for x in p: print(f'first({x.name}) = {x.first}')
for x in p: print(f'follow({x.name}) = {x.follow}')
