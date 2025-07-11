=begin
  Algoritmo de prueba robusto - Joel Orrala
  Este algoritmo permite validar el funcionamiento del analizador léxico, sintáctico y semántico
  desarrollado, cubriendo variables, tipos, operadores aritméticos y lógicos, estructura de control if-else,
  estructura de datos Hash, funciones con verificación de argumentos, clases y errores intencionales.
=end

# ----------------------------------------
# VARIABLES VÁLIDAS
nombre = "Joel"
edad = 22
salario = 1200.75
activo = true
nulo = nil

# Operaciones con variables
bono = 300
salario_total = salario + bono
descuento = 100.25
salario_neto = salario_total - descuento

# ----------------------------------------
# ESTRUCTURA DE DATOS HASH
# ✅ Hash válido
producto = { "nombre": "Laptop", "precio": 950.0, "stock": 15 }

# ❌ Hash inválido (error sintáctico)
producto_mal = { "nombre" "Laptop", "precio": 950.0 }  # ❌ ERROR SINTÁCTICO

# ----------------------------------------
# OPERACIONES ARITMÉTICAS Y LÓGICAS
suma = 15 + 5
resta = 30 - 8
multiplicacion = 4 * 6
division = 20 / 4
potencia = 3 ** 3
modulo = 17 % 4

mayor = suma > resta
igual = division == 5
condicion_compuesta = (suma > 10) && (resta < 30)

# ----------------------------------------
# ESTRUCTURA DE CONTROL IF-ELSE
# ✅ Correcta
if salario_neto >= 1000
  puts "Salario aceptable"
else
  puts "Salario bajo"
end

# ❌ Incorrecta (Error sintáctico: falta condición en if)
if
  puts "Esto generará un error sintáctico por falta de condición"  # ❌ ERROR SINTÁCTICO
end

# ----------------------------------------
# ESTRUCTURA DE CONTROL WHILE
i = 0
while i < 2
  puts "Ciclo while #{i}"
  i += 1
end

# ----------------------------------------
# FUNCIONES
# ✅ Declaración de función válida
def saludar(usuario)
  puts "¡Bienvenido, #{usuario}!"
end

# ✅ Llamada correcta
saludar("Joel")

# ❌ Llamada incorrecta (faltan argumentos)
saludar()  # ❌ ERROR SEMÁNTICO

# ----------------------------------------
# FUNCIONES CON VERIFICACIÓN DE ARGUMENTOS
# ✅ Definición
def restar(a, b)
  return a - b
end

# ✅ Llamada correcta
resultado_resta = restar(15, 5)

# ❌ Llamada incorrecta
resultado_error = restar(10)  # ❌ ERROR SEMÁNTICO

# ----------------------------------------
# CLASE
class Curso
  def initialize(nombre, duracion)
    @nombre = nombre
    @duracion = duracion
  end

  def mostrar
    puts "Curso: #{@nombre}, duración: #{@duracion} meses"
  end

  def error_break
    break  # ❌ ERROR SEMÁNTICO
  end
end

curso1 = Curso.new("Ruby", 3)
curso1.mostrar

# ----------------------------------------
# ERROR SEMÁNTICO: suma entre string y número
total_pago = "300" + 50  # ❌ ERROR SEMÁNTICO

# ----------------------------------------
# OTRAS OPERACIONES PARA PROBAR COMPATIBILIDAD
# ✅ Correctas
num1 = 8
num2 = 2
suma_correcta = num1 + num2
division_correcta = num1 / num2
potencia_correcta = num1 ** num2

# ❌ Incorrecta: operación entre tipos incompatibles
resultado_invalido = true + 5  # ❌ ERROR SEMÁNTICO

# Fin del algoritmo