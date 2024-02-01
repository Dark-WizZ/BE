import ply.lex as lex

tokens = (
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'HEADERINCLUDE',
'ID',
'OPERATOR',
'DELIMITER',
'PARENTHESIS',
'HEADER'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PARENTHESIS = r'[\(\)\{\}]'
t_DELIMITER = r'[;,]'
t_OPERATOR = r'[+\-*/=<>]'
t_ID = r'[a-zA-Z_]\w*'
t_HEADERINCLUDE=r'\#include'
t_HEADER=r'<\w+.h>'

def t_SPACE(t):
  r'\ '

def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_NEWLINE(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
  t.ignore = ' \t'

def t_error(t):
  print ("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
  
lexer = lex.lex()

data = '''
 #include<conio.h>
    if x > 5 
    {
        y = 10;
    } else {
        y = 5;
    }
    print(y);
'''

lexer.input(data)

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)
