=begin
  Caso de prueba RubyCodeAnalyzer - Avance Final
  Cubre:
  ✅ Variables y tipos
  ✅ Arrays y hash (Luis Luna)
  ✅ Operadores compuestos (Luis Luna)
  ✅ Break fuera/dentro de bucle (Luis Luna)
  ✅ Ingreso de datos por teclado (Luis Luna)
  ✅ Funciones y argumentos
  ✅ Errores léxicos, sintácticos y semánticos
=end

# VARIABLES
x = 5
y = 3.14
texto = "hola"
flag = true
nada = nil

# ASIGNACIONES CON OPERADORES COMPUESTOS (Luis Luna)
x += 2     # Válido
texto += " mundo"  # ERROR semántico: no se puede sumar string y número

# ARRAYS (Luis Luna)
nums = [1, 2, 3, 4]       # Array válido
palabras = ["uno", "dos", 3] # Array válido (tipado dinámico)
invalid_arr = [1, , 2]    # ERROR sintáctico (coma extra)

# HASH (Luis Luna)
persona = { "nombre": "Luis", "edad": 21 }
error_hash = { "a" 1, "b": 2 } # ERROR sintáctico: falta dos puntos

# INPUT (Luis Luna)
nombre = gets.chomp      # Válido
edad = gets.to_i         # Válido
dato = gets.unknown      # ERROR semántico: método no permitido

# BREAK FUERA DE BUCLE (Luis Luna)
break      # ERROR semántico: break fuera de un bucle

# BUCLE CON BREAK (Luis Luna)
for i in (1..3)
  puts i
  break   # Válido: break dentro de bucle
end

# FUNCIONES
def suma(a, b)
  return a + b
end

resultado = suma(5, 2)    # Correcto
resultado2 = suma(5)      # ERROR semántico: argumentos insuficientes

# CLASE SIMPLE
class Prueba
  def error_break
    break     # ERROR semántico: break fuera de bucle
  end
end

# OPERADORES ARITMÉTICOS
z = x + y
w = x * "hola"      # ERROR semántico: tipos incompatibles

# ESTRUCTURAS DE CONTROL
if flag
  puts "Es verdadero"
else
  puts "Es falso"
end

if x > 3 && y < 4
  puts "Rango válido"
end

if "hola"
  puts "Esto es semánticamente incorrecto"  # ERROR semántico: condición no booleana
end

# FIN DE CASO DE PRUEBA
