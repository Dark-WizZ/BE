import ply.lex as lex

tokens = (
  'Imports',
  'String',
  'Keyword',
  'Function',
  'Integer',
  'Float',
  'Operators',
  'ID',
  'LParan',
  'RParen',
  'Seperator',
  'LBrace',
  'RBrace',
)

t_Imports=r'<stdio.h>|<conio.h>|<stdlib.h>'
t_String= r'\".*\"'
t_Keyword= r"\#include|if|else|for|break|int|void|String"
t_Function=r'printf|scanf|clrscr|getch'
t_Integer= r'\d+'
t_Float= r'\d+\.\d+'
t_Operators= r'\+|\-|\/|\*|\=|<|>|==|>=|<='
t_ID= r'[a-zA-z_][a-zA-z_0-9]*'
t_LParan=r'\('
t_RParen=r'\)'
t_Seperator=r'[;,]'
t_LBrace=r'\{'
t_RBrace=r'\}'
t_ignore=r' |\t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print('error at => ',t.value[0])
  t.lexer.skip(1)

code = open('ex01.c').read()
lexer = lex.lex()
lexer.input(code)

tok=lexer.token()
while tok:
  print(tok)
  tok = lexer.token()
