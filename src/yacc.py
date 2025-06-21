import ply.yacc as yacc
import os
from datetime import datetime

# Get the token map from the lexer.  This is required.
from main import tokens

#Joel Orrala y Genesis Pacheco - Funciones con y sin parámetros
def p_function(p):
    '''function : DEF ID body END
                | DEF ID LPAREN args_multiple RPAREN body END
                | DEF ID LPAREN args RPAREN body END'''

def p_args_multiple(p):
    'args_multiple : ID COMMA args'
    p[0] = [p[1]] + p[3]


#Luis Luna
def p_args(p):
    'args : ID'

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
        | range_incl
        | range_excl
        | hash
        | function'''

#Genesis Pacheco
def p_assignment (p):
    'assignment : ID ASSIGN factor'

# Luis Luna - Inicio de la regla sintáctica para Ingreso de datos por teclado
def p_input(p):
    '''input : PUTS STRING
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

def p_term_exponent(p):     #Genesis Pacheco
    'term : term EXPONENT factor'
    #p[0] = p[1] ** p[3]

def p_term_module(p):       #Genesis Pacheco
    'term : term MODULE factor'
    #p[0] = p[1] % p[3]

def p_term_factor(p):
    'term : factor'
    #p[0] = p[1]

def p_factor_valor(p):
    '''factor : INTEGER
                | FLOAT
                | STRING
                | BOOLEAN
                | ID'''

# Luis Luna - Inicio de la regla sintáctica para estructura de datos array
def p_array(p):
    'array : ID ASSIGN LCORCH elements RCORCH'

def p_elements(p):
    '''elements : factor
                | factor COMMA elements'''
#Luis Luna - Fin de la regla sintáctica para estructura de datos array

def p_for_loop(p):  #Luis Luna
    'for_loop : FOR ID IN range_incl body END'

# def p_empty(p):
#     'empty :'
#     pass

#def p_factor_expr(p):
    #'factor : STRING'
    #p[0] = p[2]

#Joel Orrala - Estructura de datos tipo Hash
def p_hash(p):
    'hash : ID ASSIGN LBRACE hash_pairs RBRACE'

def p_hash_pairs(p):
    '''hash_pairs : STRING COLON factor
                  | STRING COLON factor COMMA hash_pairs'''
#Joel Orrala

#Genesis Pacheco - Estructura de control While
def p_while_loop(p):  #Luis Luna
    'while_loop : WHILE logic_expression body END'
#Genesis Pacheco - Fin Estrctura de control While

#Genesis Pacheco - Estructura de datos Range
def p_range_incl(p):
    'range_incl : LPAREN INTEGER RANGE_INCL INTEGER RPAREN'

def p_range_excl(p):
    'range_excl : LPAREN INTEGER RANGE_EXCL INTEGER RPAREN'

#Genesis Pacheco - Fin Estructura de datos Range

#Joel Orrala - Estructura de control if-else con condiciones lógicas
def p_condition(p):
    '''condition : IF logic_expression body END
                 | IF logic_expression body ELSE body END'''

def p_logic_expression(p):
    '''logic_expression : factor logic_op factor
                        | factor logic_op factor logic_connector logic_expression'''

def p_logic_op(p):
    '''logic_op : EQUALS
                | NEQUALS
                | GREATEREQ
                | LESSEQ
                | GREATERT
                | LESST'''

def p_logic_connector(p):
    '''logic_connector : AND
                       | OR'''
#Joel Orrala

# # Joel Orrala - Inicio de bloque de generación de logs sintácticos
# nombre_usuario = "ggpachec"  # Cambiar por el nombre de cada usuario Git
# archivo_prueba = r"..\src\algoritmos\algoritmo_genesis.rb" # Cambiar al archivo Ruby de prueba
#
# os.makedirs("logs", exist_ok=True)
#
# with open(archivo_prueba, "r", encoding="utf-8") as f:
#     data = f.read()
#
# now = datetime.now()
# fecha_hora = now.strftime("%d%m%Y-%Hh%M")
# log_filename = f"src/logs/sintactico-{nombre_usuario}-{fecha_hora}.txt"
#
# def p_error(p):
#     with open(log_filename, "w", encoding="utf-8") as log:
#         if p:
#             mensaje = f"Syntax error at token '{p.value}' (type {p.type}) at line {p.lineno}\n"
#             print(mensaje.strip())
#             log.write(mensaje)
#         else:
#             mensaje = "Syntax error at EOF\n"
#             print(mensaje.strip())
#             log.write(mensaje)
#
# # Build the parser
# parser = yacc.yacc()
# parser.parse(data)
# print(f"\nErrores sintácticos de {nombre_usuario} guardados en: {log_filename}")
# # Joel Orrala - Fin de bloque de generación de logs sintácticos



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