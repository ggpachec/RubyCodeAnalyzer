import ply.lex as lex
import os
from datetime import datetime

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
    ## TIPOS DE DATOS
    'INTEGER',
    'FLOAT',
    # Genesis Pacheco
    'STRING',
    'BOOLEAN',
    #'NIL',
    'ID',
    # Genesis Pacheco

    ## OPERADORES ARITMETICOS Y DE ASIGNACION
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    #LUIS! EXPONENT


    # Genesis Pacheco
    'ASSIGN',
    # Genesis Pacheco

    ## OPERADORES LOGICOS Y DE COMPARACION
    'AND_OP',
    'OR_OP',
    'NOT_OP',
    'EQUALS',
    'NEQUALS',
    'LESST',
    'GREATERT',
    'LESSEQ',
    'GREATEREQ',

    ## DELIMITADORES Y SIMBOLOS
    'LPAREN',
    'RPAREN',
    'LCORCH',
    'RCORCH',
    # Luis Luna - Inicio de aporte de nuevos tokens
    'EXPONENT',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMENT',
    # Luis Luna - Fin de aporte de nuevos tokens
    # Genesis Pacheco
    'COMMA',
    'COLON',
    # Genesis Pacheco
    # Joel Orrala
    'RANGE_INCL',
    'RANGE_EXCL'
    # Joel Orrala

)+tuple(reserved.values())



# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
# Genesis Pacheco
t_ASSIGN = r'='
t_EQUALS = r'=='
t_NEQUALS = r'!='
t_LESST = r'<'
t_GREATERT = r'>'
t_LESSEQ = r'<='
t_GREATEREQ = r'>='
t_AND_OP = r'&&'
t_OR_OP = r'\|\|'
t_NOT_OP = r'!'
t_COMMA = r','
t_COLON = r':'
# Genesis Pacheco
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

# Joel Orrala
t_RANGE_INCL = r'\.\.'
t_RANGE_EXCL = r'\.\.\.'
# Joel Orrala


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# A regular expression rule with some action code
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Joel Orrala - Corrección del token STRING para aceptar comillas simples o dobles
def t_STRING(t):
  r'(\"([^\\\"]|\\.)*\")|(\'([^\\\']|\\.)*\')'
  t.value = t.value[1:-1]  # remover comillas
  return t
# Joel Orrala

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Luis Luna - Inicio de aporte de nueva expresion regular para COMENTARIOS
def t_COMMENT(t):
    r'\#.*'
    return t
# Luis Luna - Fin de aporte de nueva expresion regular para COMENTARIOS

# Joel Orrala - Comentario multilínea (=begin ... =end)
def t_MULTILINE_COMMENT(t):
  r'=begin(.|\n)*?=end'
  pass  # se ignora
# Joel Orrala

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



# Joel Orrala - Inicio de bloque de generación de logs

nombre_usuario = "ggpachec"  # cambiar por cada usuario Git
archivo_prueba = r"\src\algoritmos\algoritmo_genesis.rb"  # cambiar por el archivo de cada uno


os.makedirs("logs", exist_ok=True) # Asegurar que la carpeta logs exista


with open(archivo_prueba, "r") as f:
   data = f.read()


now = datetime.now()
fecha_hora = now.strftime("%d-%m-%Y-%Hh%M")
log_filename = f"logs/lexico-{nombre_usuario}-{fecha_hora}.txt"

# Procesar análisis léxico y guardar log
with open(log_filename, "w") as log_file:
   lexer.input(data)
   while True:
       tok = lexer.token()
       if not tok:
           break
       print(tok)
       log_file.write(str(tok) + '\n')


print(f"\n Tokens de {nombre_usuario} guardados en: {log_filename}")
# Joel Orrala - Fin de bloque de generación de logs