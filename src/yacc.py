import ply.yacc as yacc
import os
from datetime import datetime

# Get the token map from the lexer.  This is required.
from main import tokens

#Agregar la tabla de simbolos
symbol_table = {
    "variables": {},
    "functions": {
        "conversion" : ["to_i", "to_f", "to_s"]
    }
}
semantic_errors = []
loop_counter = 0
current_function = None  # Para manejo futuro de contexto de función

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
                | DEF ID LPAREN args_opt RPAREN body END'''
    #Joel Orrala - regla semántica de retorno de funciones
    global current_function
    current_function = p[2]
    symbol_table["functions"][p[2]] = None  # Inicialmente None, luego se puede actualizar
    current_function = None

#Luis Luna
def p_arg(p):
    '''arg : ID
           | ID ASSIGN expression
           | STRING
           | INTEGER
           | FLOAT
           | BOOLEAN
           | TRUE
           | FALSE
           | NIL'''

def p_args(p):
    '''args : arg
            | arg COMMA args'''

    
def p_args_opt(p):
    '''args_opt : args
                | empty'''

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
                | function_call_args
                | methods'''

# Genesis Pacheco - Regla semántica Conversion de Tipos
def p_methods(p):
    'methods : ID DOT ID'

    # Validar conversión de tipos
    name = p[1]
    method = p[3]
    if name not in symbol_table["variables"]:
        msg = f"Semantic error: The variable {name} has not been defined."
        print(msg)
        semantic_errors.append(msg)
    else:
        if method in symbol_table["functions"]["conversion"]:
            if method == "to_i":
                p[0] = "int"
            elif method == "to_f":
                p[0] = "float"
            elif method == "to_s":
                p[0] = "str"
            else:
                msg = f"Semantic error: Method {method} not handled."
                print(msg)
                semantic_errors.append(msg)
        else:
            msg = f"Semantic error: Method {method} was not recognized."
            print(msg)
            semantic_errors.append(msg)

# Genesis Pacheco - Fin Regla semantica Conversion de Tipos

  #Joel Orrala - regla semántica de retorno de funciones
def p_return_stmt(p):
    'return_stmt : RETURN factor'
    global current_function
    expected = symbol_table["functions"].get(current_function)
    if expected and expected != p[2]:
        msg = f"Semantic error: Return type {p[2]} does not match expected {expected} in function {current_function}"
        print(msg)
        semantic_errors.append(msg)
    else:
        symbol_table["functions"][current_function] = p[2]
    
def p_break_stmt(p):
    'break_stmt : BREAK'
    #Luis Luna - Semantico: Chequeo de break usando contexto de bucles
    global loop_counter
    if loop_counter == 0:
        msg = f"Semantic error: 'break' used outside of a loop."
        print(msg)
        semantic_errors.append(msg)
    #Luis Luna - Fin Semantico: Chequeo de break usando contexto de bucles

#Genesis Pacheco
def p_assignment(p):
    '''assignment : ID ASSIGN expression
                  | VAR_INST ASSIGN expression'''
    # Luis Luna - Semantico: Chequeo de tipo en asignaciones
    name = p[1]
    value_type = p[3] 
    if value_type is not None:
        symbol_table["variables"][name] = value_type
    # Luis Luna - Fin Semantico: Chequeo de tipo en asignaciones

def p_assignment_compound(p):
    '''assignment : ID PLUS ASSIGN expression
                  | ID MINUS ASSIGN expression
                  | ID TIMES ASSIGN expression
                  | ID DIVIDE ASSIGN expression'''

    if p[4] in ["int", "float"]:
        p[0] = p[4]
        symbol_table["variables"][p[1]] = p[4]
    else:
        msg = f"Semantic error: Cannot apply assignment with {p[4]}"
        print(msg)
        semantic_errors.append(msg)

# Luis Luna - Inicio de la regla sintáctica para Ingreso de datos por teclado
def p_input(p):
    '''input : PUTS STRING
            | ID ASSIGN GETS method_chain'''
# Luis Luna - Fin de la regla sintáctica para Ingreso de datos por teclado

def p_method_chain(p):
    '''method_chain : DOT ID
                    | method_chain DOT ID'''

#Joel Orrala - regla semántica de compatibilidad en operaciones aritméticas
def p_expression_plus(p):
    'expression : expression PLUS term'
    if p[1] in ["int", "float"] and p[3] in ["int", "float"]:
        p[0] = "int" if p[1] == "int" and p[3] == "int" else "float"
    else:
        msg = f"Semantic error: Cannot apply '+' between {p[1]} and {p[3]}"
        print(msg)
        semantic_errors.append(msg)

#Joel Orrala - regla semántica de compatibilidad en operaciones aritméticas
def p_expression_minus(p):
    'expression : expression MINUS term'
    if p[1] in ["int", "float"] and p[3] in ["int", "float"]:
        p[0] = "int" if p[1] == "int" and p[3] == "int" else "float"
    else:
        msg = f"Semantic error: Cannot apply '-' between {p[1]} and {p[3]}"
        print(msg)
        semantic_errors.append(msg)

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

#Joel Orrala - regla semántica de compatibilidad en operaciones aritméticas
def p_term_times(p):
    'term : term TIMES factor'
    if p[1] in ["int", "float"] and p[3] in ["int", "float"]:
        p[0] = "int" if p[1] == "int" and p[3] == "int" else "float"
    else:
        msg = f"Semantic error: Cannot apply '*' between {p[1]} and {p[3]}"
        print(msg)
        semantic_errors.append(msg)
        
#Joel Orrala - regla semántica de compatibilidad en operaciones aritméticas    
def p_term_div(p):
    'term : term DIVIDE factor'
    if p[1] in ["int", "float"] and p[3] in ["int", "float"]:
        p[0] = "float"
    else:
        msg = f"Semantic error: Cannot apply '/' between {p[1]} and {p[3]}"
        print(msg)
        semantic_errors.append(msg)

def p_term_exponent(p):     #Genesis Pacheco
    'term : term EXPONENT factor'
    #Joel Orrala - regla semántica de compatibilidad en operaciones aritméticas
    if p[1] in ["int", "float"] and p[3] in ["int", "float"]:
        p[0] = "float"
    else:
        msg = f"Semantic error: Cannot apply '**' between {p[1]} and {p[3]}"
        print(msg)
        semantic_errors.append(msg)

def p_term_module(p):       #Genesis Pacheco
    'term : term MODULE factor'
    #Joel Orrala - regla semántica de compatibilidad en operaciones aritméticas
    if p[1] in ["int", "float"] and p[3] in ["int", "float"]:
        p[0] = "int"
    else:
        msg = f"Semantic error: Cannot apply '%' between {p[1]} and {p[3]}"
        print(msg)
        semantic_errors.append(msg)

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

#Joel Orrala para la regla sintactica / Luis Luna para la regla semantica
# Luis Luna - Semantico: Chequeo de tipo en asignaciones y uso de variables
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
    if type(p[1]) == int:
        p[0] = "int"
    elif type(p[1]) == float:
        p[0] = "float"
    elif isinstance(p[1], str) and p.slice[1].type == "STRING":
        p[0] = "str"
    elif p.slice[1].type == "TRUE" or p.slice[1].type == "FALSE":
        p[0] = "bool"
    elif p.slice[1].type == "NIL":
        p[0] = "nil"
# Luis Luna - Fin Semantico: Chequeo de tipo en asignaciones y uso de variables
    else:
        nombre = p[1]
        if nombre not in symbol_table["variables"]:
            msg = f"Semantic error: Variable '{nombre}' used without being defined."
            print(msg)
            semantic_errors.append(msg)
        else:
            p[0] = symbol_table["variables"][nombre]
#Joel Orrala           


# Joel Orrala - Para permitir expresiones agrupadas con paréntesis
def p_factor_group(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Joel Orrala - Para permitir expresiones lógicas como parte de un factor
def p_factor_logic_expression(p):
    'factor : logic_expression'
    p[0] = p[1]


    
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

# Joel Orrala - Llamada a función con punto
def p_method_call_with_dot(p):
    'expression : ID DOT ID LPAREN args_opt RPAREN'

# Luis Luna - Inicio de la regla sintáctica para estructura de datos array
def p_array(p):
    'array : ID ASSIGN LCORCH elements RCORCH'

def p_elements(p):
    '''elements : factor
                | factor COMMA elements'''
#Luis Luna - Fin de la regla sintáctica para estructura de datos array

#Luis Luna Regla sintactico y semantico: Estructura de control For / Chequeo de break usando contexto de bucles
def p_for_loop(p):
    'for_loop : FOR ID IN range_incl body END'
    global loop_counter
    loop_counter += 1
    # The body is processed as usual
    loop_counter -= 1
# Luis Luna

#Joel Orrala - Estructura de datos tipo Hash
def p_hash(p):
    'hash : ID ASSIGN LBRACE hash_pairs RBRACE'

def p_hash_pairs(p):
    '''hash_pairs : STRING COLON factor
                  | STRING COLON factor COMMA hash_pairs'''
#Joel Orrala

#Genesis Pacheco - Estructura de control While
# Luis Luna - Semantico: Chequeo de break usando contexto de bucles
def p_while_loop(p):  
    'while_loop : WHILE logic_expression body END'
    global loop_counter
    loop_counter += 1

    # Genesis Pacheco - Regla Semantica Condiciones lógicas
    condition_type = p[2]
    if condition_type not in ["bool", "int", "float"]:
        msg = f"Semantic error: WHILE condition must be boolean or evaluable, got '{condition_type}'"
        print(msg)
        semantic_errors.append(msg)
    # Genesis Pacheco - Fin Regla Semantica Condiciones Logicas
    loop_counter -= 1
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

# Genesis Pacheco - Regla Semantica Condiciones Logicas
    condition_type = p[2]
    if condition_type not in ["bool", "int", "float"]:
        msg = f"Semantic error: IF condition must be boolean, got '{condition_type}'"
        print(msg)
        semantic_errors.append(msg)


# def p_logic_expression(p):
#     '''logic_expression : factor logic_op factor
#                         | factor logic_connector factor
#                         | factor logic_op factor logic_connector logic_expression'''

def p_logic_expression_comparison(p):
    'logic_expression : factor logic_op factor'
    # Comparaciones simples (a > b, a == b)
    left = p[1]
    right = p[3]
    if left in ["int", "float"] and right in ["int", "float"]:
        p[0] = "bool"
    elif left == right:
        p[0] = "bool"
    else:
        msg = f"Semantic error: Cannot compare {left} with {right}"
        print(msg)
        semantic_errors.append(msg)
        p[0] = "error"

def p_logic_expression_connector(p):
    'logic_expression : factor logic_connector factor'
    # A and B, A or B
    if p[1] == "bool" and p[3] == "bool":
        p[0] = "bool"
    else:
        msg = f"Semantic error: Logical connector requires boolean operands. Got '{p[1]}' and '{p[3]}'"
        print(msg)
        semantic_errors.append(msg)
        p[0] = "error"


def p_logic_expression_expression(p):
    'logic_expression : expression logic_op expression'

    if p[1] in ["int", "float"] and p[3] in ["int", "float"]:
        p[0] = "bool"
    else:
        msg = f"Semantic error: Invalid comparison between {p[1]} and {p[3]}"
        print(msg)
        semantic_errors.append(msg)
        p[0] = "error"
# Genesis Pacheco - Fin Regla Semantica Condiciones Logicas


def p_logic_op(p):
    '''logic_op : EQUALS
                | NEQUALS
                | GREATEREQ
                | LESSEQ
                | GREATERT
                | LESST'''

def p_logic_connector(p):
    '''logic_connector : AND
                       | OR
                       | AND_OP
                       | OR_OP'''
    
def p_empty(p):
    'empty :'
    pass

#Joel Orrala

# Joel Orrala - Inicio de bloque de generación de logs sintácticos
nombre_usuario = "luisluna2307"  # Cambiar por el nombre de cada usuario Git
archivo_prueba =  r"C:\Github\RubyCodeAnalyzer\src\algoritmos\algoritmo_luis.rb" # Cambiar al archivo Ruby de prueba
log_dir = r"C:\Github\RubyCodeAnalyzer\src\logs"
os.makedirs(log_dir, exist_ok=True)

with open(archivo_prueba, "r", encoding="utf-8") as f:
    data = f.read()
now = datetime.now()
fecha_hora = now.strftime("%d%m%Y-%Hh%M")
#log_filename = f"..\src\logs\sintactico-{nombre_usuario}-{fecha_hora}.txt"
# Nombres de los archivos
sintactico_log = os.path.join(log_dir, f"sintactico-{nombre_usuario}-{fecha_hora}.txt")
semantico_log = os.path.join(log_dir, f"semantico-{nombre_usuario}-{fecha_hora}.txt")

# Guardar errores sintácticos
def p_error(p):
    with open(sintactico_log, "a", encoding="utf-8") as log:
        if p:
            mensaje = f"Syntax error at token '{p.value}' (type {p.type}) at line {p.lineno}\n"
            print(mensaje.strip())
            log.write(mensaje)
        else:
            mensaje = "Syntax error at EOF\n"
            print(mensaje.strip())
            log.write(mensaje)
    print(f"\nErrores sintácticos de {nombre_usuario} guardados en: {sintactico_log}")

# Build the parser
parser = yacc.yacc(start='start')
parser.parse(data)

# Genesis Pacheco - Guardar errores semánticos
with open(semantico_log, "a", encoding="utf-8") as log:
    if len(semantic_errors) == 0:
        log.write("No semantic errors found.\n")
    else:
        for error in semantic_errors:
            log.write(error + "\n")
        print(f"\nErrores semánticos de {nombre_usuario} guardados en: {semantico_log}")

# Joel Orrala - Fin de bloque de generación de logs sintácticos

# Impresiones de validacion
print(len(semantic_errors))
print(semantic_errors)
print(symbol_table)


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