# Algoritmo de prueba para el analizador léxico en Ruby
# Comentario de una sola línea

# Definición de variables
edad = 25               # Variable de tipo Integer
nombre = "Luis"         # Variable de tipo String
activo = true           # Variable de tipo Boolean
temperatura = 23.5      # Variable de tipo Float

# Casos incorrectos
1edad = 30              # ERROR: Variable no puede empezar con un número
nombre = "Carlos'       # ERROR: Comillas no cerradas en el String
activo = "verdadero"    # ERROR: Asignación de String a un Boolean
temperatura = "veintitres"  # ERROR: Asignación de String a un Float

# Estructura de control (if-else)
if edad >= 18
    puts "Mayor de edad"
else
    puts "Menor de edad"
end

# Casos incorrectos
if 18 >= edad            # ERROR: Operación lógica con tipos incorrectos
    puts "Este es un error"
end

# Operaciones aritméticas
suma = 10 + 5
resta = 10 - 4
multiplicacion = 6 * 2
division = 10 / 2
potencia = 2 ** 3       # Exponente

# Casos incorrectos
suma = 10 + "5"         # ERROR: No se puede sumar un Integer con un String
multiplicacion = "2" * 2  # ERROR: No se puede multiplicar un String con un Integer

# Operaciones lógicas
es_valido = true && false
es_igual = nombre == "Luis"

# Casos incorrectos
es_valido = "true" && false  # ERROR: String no se puede combinar con Boolean
es_igual = 10 == "Luis"      # ERROR: Comparación entre tipos incompatibles

# Operaciones de comparación
mayor = edad > 18
igual = nombre == "Luis"
diferente = edad != 30

# Casos incorrectos
mayor = edad > "18"          # ERROR: Comparación de tipos incompatibles
igual = "Luis" == true       # ERROR: Comparación de String con Boolean

# Estructura de control (for)
for i in 1..5
    puts i
end

# Casos incorrectos
for i in "1..5"             # ERROR: El rango no puede ser un String
    puts i
end

# Uso de rangos (inclusive y exclusivo)
rango_incl = (1..5)   # Rango inclusivo
rango_excl = (1...5)  # Rango exclusivo

# Casos incorrectos
rango_incl = (1..5)   # ERROR: Rango no es válido si no se asigna adecuadamente
rango_excl = [1...5]  # ERROR: El rango debería estar en un formato correcto

# Comentario multilínea
=begin
Este es un comentario
multilínea en Ruby.
=end

# Casos incorrectos
=begin
Este es un comentario sin finalizar correctamente
=end

# Fin del algoritmo
