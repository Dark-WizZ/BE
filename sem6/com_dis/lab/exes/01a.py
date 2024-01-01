import re

def lex_anz(input):
    tokens = []
    keywords = ['if', 'else', 'while', 'for', 'int', 'float']

    patterns = {
        'NUMBER': r'\d+(\.\d+)?',
        'ID': r'[a-zA-Z_]\w*',
        'OPERATOR': r'[+\-*/=<>]',
        'DELIMITER': r'[;,]',
        'PARENTHESIS': r'[\(\)\{\}]'
    }

    regex_patt = '|'.join(f'(?P<{tok}>{patterns[tok]})' for tok in patterns)
    for match in re.finditer(regex_patt, input):
        tok_type = match.lastgroup
        tok_val = match.group()

        if tok_val in keywords:
            tok_type = 'KEYWORD'


        tokens.append((tok_type, tok_val))

    return tokens
    
code = 'if x > 5 { y = 10; } else { y = 5; }'
result = lex_anz(code)
for t, v in result: print(f'{v} -> {t}')
