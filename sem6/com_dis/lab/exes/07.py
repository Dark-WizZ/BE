# example 1
gram = {
    "S": ["S+S", "S*S",'S-S','(S)', "id"]
}
start = "S"
inp = "id+id-(id+id)$"
stack = "$"
print(f'{"Stack": <15}' + "|" + f'{"Input Buffer": <15}' + "|" + 'Parsing Action')
print(f'{"-":-<50}')
while True:
    action = True
    i = 0
    while i < len(gram[start]):
        if gram[start][i] in stack:
            stack = stack.replace(gram[start][i], start)
            print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + f'Reduce > {gram[start][i]}')
            i = -1
            action = False
        i += 1
    if len(inp) > 1:
        stack += inp[0]
        inp = inp[1:]
        print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + 'Shift')
        action = False
    if inp == "$" and stack == ("$" + start):
        print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + 'Accepted')
        break
    if action:
        print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + 'Rejected')
        break
