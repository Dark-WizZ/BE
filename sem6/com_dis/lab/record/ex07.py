gram = { 'S':['S+S','S-S','S*S','(S)','id']}
start='S'
inp='id+id$'
stack='$'
print(f'{"Stack":<15}|{"Input Buffer":<15}|Parsing Action')

while True:
  flag=1
  for i in gram[start]:
    if i in stack:
      flag=0
      stack = stack.replace(i, start)
      print(f'{stack:<15}|{inp:<15}|Reduce {start} -> {i}')
  if len(inp)>1:
      flag=0
      stack+=inp[0]
      inp=inp[1:]
      print(f'{stack:<15}|{inp:<15}|Shift')
  if inp=='$' and stack=='$'+start:
      print(f'{stack:<15}|{inp:<15}|Accepted')
      break
  if flag:
      print(f'{stack:<15}|{inp:<15}|Rejected')
      break
    