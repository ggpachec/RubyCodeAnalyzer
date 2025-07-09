=begin
  Algoritmo de prueba - Joel Orrala
  Cubre variables, tipos, operadores, estructuras de control, funciones, clases, y errores léxicos/sintácticos
=end

# Variables válidas
nombre = "Joel"
_edad = 22
salario_mensual = 1000.50
activo = true
nulo = nil

# Variables inválidas
1invalida = 30        # ERROR léxico: comienza con número
@variable_local = 40  # ERROR léxico: variable de instancia mal usada si se prohíbe

# Array, Hash y Range
numeros = [1, 2, 3, 4]
persona = { "nombre": "Ana", "edad": 25 }
rango = (1..5)

# Operaciones aritméticas y lógicas
suma = 10 + 5
potencia = 2 ** 3
division = 9 / 3
es_mayor = (suma > 10) && (potencia < 10)

# Estructuras de control
if suma >= 15
  puts "Suma alta"
else
  puts "Suma baja"
end

for i in 1..3
  puts "Iteración #{i}"
end

i = 0
while i < 2
  puts "while loop #{i}"
  i += 1
end

# Declaración de funciones
def saludar(nombre = "Usuario")
  puts "Hola, #{nombre}"
end

def dividir(a, b)
  return a / b
end

saludar("Joel")
resultado = dividir(10, 2)

# Error semántico: suma entre string y número
total = "500" + 20  # ERROR semántico

# Clase
class Estudiante
  def initialize(nombre, edad)
    @nombre = nombre
    @edad = edad
  end

  def presentar
    puts "Soy #{@nombre} y tengo #{@edad} años"
  end

  def error_break
    break  # ERROR: break fuera de un bucle
  end
end

est1 = Estudiante.new("Carla", 21)
est1.presentar

# Error léxico: comillas mal cerradas
mensaje = "Este string no se cierra  # ERROR léxico

# Fin del algoritmo
