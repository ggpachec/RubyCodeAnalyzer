# Yacc example
import datetime as dt
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from main import tokens


# CAMBIAR Y RECORDAR que EQUALS y ASSIGN son diferentes en el contexto 
# del lexer y del token que definimos
#t_EQUALS = r'=='
#t_ASSIGN = r'='

def p_function(p):                                          #Genesis Pacheco
    '''function : DEF ID LPAREN RPAREN
    | DEF ID LPAREN body RPAREN'''
    
#Luis Luna
def args(p):
    '''args : ID
            | ID COMMA args
            | empty'''

def p_body(p):
    '''body : sentence
        | sentence body'''

def p_print(p):
    'print : PUTS  factor'

def p_sentence(p):
    '''sentence : assignment
        | expression
        | print
        | input
        | condition
        | while_loop
        | for_loop
        | array
        | range
        | function
        | class_def'''

#CAMBIAR A ASSIGN
def p_assignment (p):                                       #Genesis Pacheco
    'assignment : ID EQUALS factor'

# Luis Luna - Inicio de la regla sintáctica para Ingreso de datos por teclado
def p_input(p):
    ''''input : PRINT STRING
            | ID ASSIGN GETS DOT ID'''
# Luis Luna - Fin de la regla sintáctica para Ingreso de datos por teclado


def p_expression_plus(p):
    'expression : expression PLUS term'
    #p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    #p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    #p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    #p[0] = p[1] * p[3]
    
def p_term_div(p):
    'term : term DIVIDE factor'
    #p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    #p[0] = p[1]

#def p_factor_integer(p):
 #   'factor : INTEGER'
  #  p[0] = p[1]

#def p_factor_float(p):
 #   'factor : FLOAT'
  #  p[0] = p[1]


def p_factor_valor(p):
    '''factor : INTEGER
                | FLOAT
                | STRING
                | BOOLEAN
                | ID'''

# Luis Luna - Inicio de la regla sintáctica para estructura de datos array
def p_array(p):
    '''array : ID ASSIGN LCORCH elements RCORCH'''

def p_elements(p):
    '''elements : factor
                | factor COMMA elements'''
#Luis Luna - Fin de la regla sintáctica para estructura de datos array

def p_for_loop(p):  #Luis Luna
    'for_loop : FOR ID IN range body END'
    
def p_range(p): #Luis Luna
    'range : LPAREN INTEGER RANGE_INCL INTEGER RPAREN'

def p_empty(p):
    'empty :'
    pass

def p_factor_expr(p):
    'factor : STRING'
    #p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (type {p.type}) at line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('Ruby > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)