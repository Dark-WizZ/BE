import re

ip = input("Enter production: ")
name, prods = ip.split(' -> ')
prods = prods.split(' | ')

terminals=r'[a-z\(\)\+\-\*\/]'
lead=[]
trail=[]
for p in prods:
    for c in p:
        if re.match(re.compile(terminals),c):
            lead.append(c)
            break
    for c in reversed(p):
        if re.match(re.compile(terminals),c):
            trail.append(c)
            break
print('leading set: ',lead)
print('trailing set: ',trail)
