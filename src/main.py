import ply.lex as lex

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'def' : 'DEF',
    'class' : 'CLASS',
    'return' : 'RETURN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    # Luis Luna - Inicio de aporte de palabras reservadas
    'nil': 'NIL',
    'end' : 'END',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'next' : 'NEXT',
    'break' : 'BREAK',
    'yield' : 'YIELD',
    'module' : 'MODULE',
    'do' : 'DO',
    #Luis Luna - Fin de aporte de palabras reservadas
}

# List of token names.   This is always required
tokens = (
    'INTEGER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MODULE',
    'LCORCH',
    'RCORCH',
    'ID',
    'STRING',
    # Luis Luna - Inicio de aporte de nuevos tokens
    'EXPONENT',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    # Luis Luna - Fin de aporte de nuevos tokens
)+tuple(reserved.values())



# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MODULE = r'%'
t_LCORCH = r'\['
t_RCORCH = r'\]'
# Luis Luna - Inicio de aporte de nuevas expresiones regulares para tokens simples
t_EXPONENT = r'\*\*'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
# Luis Luna - Fin de aporte de nuevas expresiones regulares para tokens simples


def t_FLOAT(t):
    r'd+\.\d+'
    t.value = float(t.value)
    return t

# A regular expression rule with some action code
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'¨[^¨]*¨'
    t.value = str(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Luis Luna - Inicio de aporte de nueva expresion regular para COMENTARIOS
def t_COMMENT(t):
    r'#.*'
    return t
# Luis Luna - Fin de aporte de nueva expresion regular para COMENTARIOS


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()



# Test it out
data = '''
3 + 4 * 10
def aaa * 5
def ¨D¨ DD¨
def ¨¨
  + -20 *2
  10.5
  5
  10,6
  %
  [
  ]
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
