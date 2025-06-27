import ply.yacc as yacc
import os
from datetime import datetime

# Get the token map from the lexer.  This is required.
from main import tokens

# Joel Orrala: Regla inicial del parser
def p_start(p):
    'start : sentences'

def p_sentences(p):
    '''sentences : sentence
                 | sentence sentences'''
# Joel Orrala
    
#Joel Orrala y Genesis Pacheco - Funciones con y sin parámetros
def p_function(p):
    '''function : DEF ID body END
                | DEF ID LPAREN args RPAREN body END'''


#Luis Luna
def p_args(p):
    '''args : ID
            | ID COMMA args'''

def p_body(p):
    '''body : body sentence
            | sentence'''

def p_print(p):
    '''print : PUTS factor
                | PUTS STRING'''

#Joel Orrala
def p_class_def(p):
    '''class_def : CLASS ID body END'''
#Joel Orrala

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
                | function
                | class_def
                | return_stmt
                | break_stmt
                | function_call_empty
                | function_call_args'''

def p_return_stmt(p):
    'return_stmt : RETURN factor'
    
def p_break_stmt(p):
    'break_stmt : BREAK'

#Genesis Pacheco
def p_assignment(p):
    '''assignment : ID ASSIGN expression
                  | VAR_INST ASSIGN expression'''

# Luis Luna - Inicio de la regla sintáctica para Ingreso de datos por teclado
def p_input(p):
    '''input : PUTS STRING
            | ID ASSIGN GETS method_chain'''
# Luis Luna - Fin de la regla sintáctica para Ingreso de datos por teclado

def p_method_chain(p):
    '''method_chain : DOT ID
                    | method_chain DOT ID''' 


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

#Joel Orrala
def p_factor_valor(p):
    '''factor : INTEGER
                | FLOAT
                | STRING
                | BOOLEAN
                | ID
                | VAR_INST
                | TRUE
                | FALSE
                | NIL'''
#Joel Orrala           


# Joel Orrala - Para permitir expresiones agrupadas con paréntesis
def p_factor_group(p):
    'factor : LPAREN expression RPAREN'
    #p[0] = p[2]

# Joel Orrala - Para permitir expresiones lógicas como parte de un factor
def p_factor_logic_expression(p):
    'factor : logic_expression'
    #p[0] = p[1]


    
def p_factor_range_incl(p):
    'factor : range_incl'

def p_factor_range_excl(p):
    'factor : range_excl'


# Joel Orrala - Llamada a función sin argumentos
def p_function_call_empty(p):
    'function_call_empty : ID LPAREN RPAREN'
    #p[0] = ('func_call', p[1], [])

# Joel Orrala - Llamada a función con argumentos
def p_function_call_args(p):
    'function_call_args : ID LPAREN args RPAREN'
    #p[0] = ('func_call', p[1], p[3])


# Luis Luna - Inicio de la regla sintáctica para estructura de datos array
def p_array(p):
    'array : ID ASSIGN LCORCH elements RCORCH'

def p_elements(p):
    '''elements : factor
                | factor COMMA elements'''
#Luis Luna - Fin de la regla sintáctica para estructura de datos array

def p_for_loop(p):  #Luis Luna
    'for_loop : FOR ID IN range_incl body END'

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
    '''range_incl : LPAREN INTEGER RANGE_INCL INTEGER RPAREN
                    | INTEGER RANGE_INCL INTEGER'''

def p_range_excl(p):
    '''range_excl : LPAREN INTEGER RANGE_EXCL INTEGER RPAREN
                | INTEGER RANGE_EXCL INTEGER'''

#Genesis Pacheco - Fin Estructura de datos Range

#Joel Orrala - Estructura de control if-else con condiciones lógicas
def p_condition(p):
    '''condition : IF logic_expression body END
                 | IF logic_expression body ELSE body END'''

def p_logic_expression(p):
    '''logic_expression : factor logic_op factor
                        | factor logic_op factor logic_connector logic_expression'''

def p_logic_expression_expression(p):
    'logic_expression : expression logic_op expression'


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

# Joel Orrala - Inicio de bloque de generación de logs sintácticos
nombre_usuario = "luisluna2307"  # Cambiar por el nombre de cada usuario Git
archivo_prueba =  r"C:\Github\RubyCodeAnalyzer\src\algoritmos\algoritmo_luis.rb" # Cambiar al archivo Ruby de prueba

os.makedirs("logs", exist_ok=True)

with open(archivo_prueba, "r", encoding="utf-8") as f:
    data = f.read()
now = datetime.now()
fecha_hora = now.strftime("%d%m%Y-%Hh%M")
log_filename = f"src/logs/sintactico-{nombre_usuario}-{fecha_hora}.txt"

def p_error(p):
    with open(log_filename, "w", encoding="utf-8") as log:
        if p:
            mensaje = f"Syntax error at token '{p.value}' (type {p.type}) at line {p.lineno}\n"
            print(mensaje.strip())
            log.write(mensaje)
        else:
            mensaje = "Syntax error at EOF\n"
            print(mensaje.strip())
            log.write(mensaje)

# Build the parser
parser = yacc.yacc(start='start')
parser.parse(data)
print(f"\nErrores sintácticos de {nombre_usuario} guardados en: {log_filename}")
# Joel Orrala - Fin de bloque de generación de logs sintácticos

#ELIMINAR ESTE P_ERROR AL ELIMINAR EL WHILE DE DEBAJO
#def p_error(p):
#    if p:
#        print(f"yacc: Syntax error at line {p.lineno}, token={p.type}")
#    else:
#        print("yacc: Parse error in input. EOF")


# Build the parser
#parser = yacc.yacc(start='start')
#
#while True:
#   try:
#       s = input('calc > ')
#   except EOFError:
#       break
#   if not s: continue
#   result = parser.parse(s)
#   print(result)