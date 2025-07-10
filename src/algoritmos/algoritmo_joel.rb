=begin
  Algoritmo de prueba actualizado - Joel Orrala
  Cubre:
  ✅ Variables y tipos
  ✅ Operadores aritméticos y lógicos
  ✅ Estructuras de control (if-else)
  ✅ Estructura de datos Hash
  ✅ Funciones con verificación de argumentos
  ✅ Clases
  ✅ Errores léxicos, sintácticos y semánticos
=end

# ----------------------------------------
# VARIABLES VÁLIDAS
nombre = "Joel"
edad = 22
salario = 1000.50
activo = true
nulo = nil

# Operaciones con variables válidas
bono = 200
salario_total = salario + bono

# ----------------------------------------
# VARIABLES INVÁLIDAS (Errores léxicos)
1variable = 10          # ❌ ERROR LÉXICO: inicia con número
@variable_local = 30    # ❌ ERROR LÉXICO: variable de instancia 
$incorrecto = "test"    # ❌ ERROR LÉXICO: variable global 

# ----------------------------------------
# ESTRUCTURA DE DATOS HASH
# ✅ Hash válido
persona = { "nombre": "Ana", "edad": 25, "activo": true }

# ❌ Hash inválido (falta dos puntos)
persona_mal = { "nombre" "Ana", "edad": 25 }  # ❌ ERROR SINTÁCTICO

# ----------------------------------------
# OPERACIONES ARITMÉTICAS Y LÓGICAS
suma = 10 + 5
resta = 20 - 4
multiplicacion = 3 * 7
division = 14 / 2
potencia = 2 ** 3
modulo = 10 % 3

es_mayor = suma > resta
es_igual = suma == 15
combinacion = (suma > 5) && (division < 10)

# ----------------------------------------
# ESTRUCTURA DE CONTROL IF-ELSE
# ✅ Correcta
if suma >= 15
  puts "Suma alta"
else
  puts "Suma baja"
end

# ❌ Incorrecta (Error sintáctico: falta 'end')
if suma >= 15
  puts "Este bloque no tiene 'end', provocando un error sintáctico"  # ❌ ERROR SINTÁCTICO

# ----------------------------------------
# ESTRUCTURA DE CONTROL WHILE
contador = 0

# ✅ Correcta
while contador < 3
  puts "Iteración #{contador}"
  contador += 1
end

# ----------------------------------------
# FUNCIONES
# ✅ Declaración de función válida
def saludar(nombre)
  puts "Hola, #{nombre}"
end

# ✅ Llamada correcta
saludar("Joel")

# ❌ Llamada incorrecta (faltan argumentos)
saludar()  # ❌ ERROR SEMÁNTICO: argumentos insuficientes

# ----------------------------------------
# FUNCIONES CON VERIFICACIÓN DE ARGUMENTOS
# ✅ Definición con dos parámetros
def dividir(a, b)
  return a / b
end

# ✅ Llamada con dos argumentos
resultado = dividir(10, 2)

# ❌ Llamada con un argumento
resultado_error = dividir(10)  # ❌ ERROR SEMÁNTICO: argumentos insuficientes

# ----------------------------------------
# CLASE
class Estudiante
  def initialize(nombre, edad)
    @nombre = nombre
    @edad = edad
  end

  def presentar
    puts "Soy #{@nombre} y tengo #{@edad} años"
  end

  def error_break
    break  # ❌ ERROR SEMÁNTICO: 'break' fuera de un bucle
  end
end

# Instanciación y uso correcto
est1 = Estudiante.new("Carla", 21)
est1.presentar

# ----------------------------------------
# ERROR SEMÁNTICO: suma entre string y número
total = "500" + 20  # ❌ ERROR SEMÁNTICO: tipos incompatibles en suma

# Fin del algoritmo