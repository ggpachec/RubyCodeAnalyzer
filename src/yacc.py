# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from main import tokens

def p_function(p):                                          #Genesis Pacheco
    '''function : DEF ID LPAREN RPAREN
    | DEF ID LPAREN body RPAREN'''

def p_body(p):
    '''body : sentence
        | sentence body'''

def p_print(p):
    'print : PUTS  factor'

def p_sentence(p):
    '''sentence : assignment
        | expression
        | print'''


def p_assignment (p):                                       #Genesis Pacheco
    'assignment : ID EQUALS factor'


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
                | ID'''



def p_factor_expr(p):
    'factor : STRING'
    #p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)