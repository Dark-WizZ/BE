import re

input = 'a a* ( a ( i / p ) s a ) o / p'
print(input)

patterns = {
    'paren' : '\(.*\)',
    'or' : '\/',
    'astar' : '[a-z]\*',
    'a' : '[a-z]',
}

res = []

def tokenize(input):
    regex_patt = '|'.join(f'(?P<{tok}>{patterns[tok]})' for tok in patterns)
    temp=[]
    for match in re.finditer(regex_patt, input):
        group = match.lastgroup
        value = match.group()
        if(group=='paren'):
            tokenize(value[1:-1])
        else:
            temp.append(value)
    res.append(temp)
    print(res)
    
tokenize(input)
