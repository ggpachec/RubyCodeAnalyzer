# Prueba de variables y asignaciones
edad = 28
nombre = "Ana"
activo = true
temperatura = 21.7
arreglo = [1, 2, 3, 4]
persona = { "nombre": "Ana", "edad": 28 }
rango_incl = (1..5)
rango_excl = (1...5)
@instancia = "Soy una variable de instancia"

# Impresión y entrada de datos
puts "Ingrese su apellido:"
apellido = gets.chomp

# Expresiones aritméticas y booleanas
resultado = (edad + 2) * 3 - 1
es_adulto = edad >= 18 && activo

# Estructura de control if-else
if edad >= 18
    puts "Es mayor de edad"
else
    puts "Es menor de edad"
end

# Bucle while
contador = 0
while contador < 3
    puts contador
    contador = contador + 1
end

# Bucle for con rango
for i in 1..5
    puts i
end

# Definición de función sin parámetros
def saludar
    puts "Hola!"
end

# Definición de función con parámetros y return
def sumar(a, b)
    resultado = a + b
    return resultado
end

# Llamada a función
saludar()
total = sumar(5, 3)

# Definición de clase con método y propiedades
class Persona
    def initialize(nombre, edad)
        @nombre = nombre
        @edad = edad
    end

    def saludar
        puts "Hola, soy #{@nombre} y tengo #{@edad} años"
    end
end

ana = Persona.new("Ana", 28)
ana.saludar()

# Comentarios de una línea y multilínea
# Este es un comentario de una línea

=begin
Este es un comentario
de varias líneas.
=end

# --------------------
# Errores SINTÁCTICOS INTENCIONALES para probar el parser:
# 1. Bloque if sin end
if activo
    puts "Bloque if sin end"
# Falta end aquí

# 2. Bucle while mal cerrado
while contador < 5
    puts contador
    contador += 1
# Falta end aquí

# 3. Llamada a función sin paréntesis (no permitido según tu gramática actual)
saludar

# 4. Array mal formado (falta corchete de cierre)
numeros = [1, 2, 3

# 5. Hash mal formado (falta llave de cierre)
mascota = { "nombre": "Toby", "edad": 2

# 6. Asignación sin expresión
total =

# 7. Paréntesis desbalanceados
resultado = (5 + 2

# 8. Uso incorrecto de else
else
    puts "Error de else sin if"
end

# 9. Llamada a función con coma de más
sumar(4, 5,)

# 10. Operador aritmético sin operando
diferencia = 10 -

