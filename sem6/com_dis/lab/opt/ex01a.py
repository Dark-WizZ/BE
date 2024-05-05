import re

patts = {
  'Imports': r"<\w*\.h>",
  'String' : r'".*"',
  'Keyword' : r"#include|if|else|for|break|int|void|String",
  'Function': r'printf|scanf|clrscr|getch',
  'Integer' : r'\d+',
  'Float' : r'\d+\.\d+',
  'Operators' : r'[\+\-\/\*\=<>]|==|>=|<=',
  'ID' : r'[a-zA-z_][a-zA-z_0-9]*',
  'LParan':r'\(',
  'RParen':r'\)',
  'Seperator':r'[;,]',
  'LBrace':'\{',
  'RBrace':'\}',
}

def lex_anz(input):
  tokens = []

  regex_patt = '|'.join(f'(?P<{t}>{p})'for t,p in patts.items())
  for match in re.finditer(regex_patt, input):
    tok_type  = match.lastgroup
    tok_value = match.group()
    tokens.append((tok_type,tok_value))
  return tokens

code = open('ex01.c').read()
result = lex_anz(code)
for t,v in result: print(f'{v} -> {t}')