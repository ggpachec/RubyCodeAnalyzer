#CASO DE PRUEBA- GENESIS PACHECO

=begin
Este código incluye fragmentos correctos e incorrectos,
organizados por secciones.
=end

## SECCION 1: DECLARACION DE VARIABLES

nombre = "María"                 # ✅ Simple
edad_correcta = 10               # ✅ Numérica
resultado = edad_correcta + 5    # ✅ Con expresión
Edad = 10                        #
edad = "10"+5                    # ❌ Error semántico: String asignado a una variable usada como número
2variable = "dato"
_1nombres = "Inválido"


## SECCION 2: TIPOS DE DATOS

# Tipos Primitivos
entero = 100                     # ✅ Integer
decimal = 3.1415                 # ✅ Float
texto = "Hola mundo"             # ✅ String
activo = true                    # ✅ Boolean
nulo = nil                       # ✅ Nil

# Tipos Estructurados
# Hash
usuario = { "nombre" : "Ana", "edad" : 28 }   # ✅ Hash correcto
persona = { nombre : "Luis", edad : 30 }      # ❌ Error sintáctico : nombre no es String

# Array
numeros_primos = [2, 3, 5, 7, 11, 13]           # ✅ Array

# Range
rango_10 = (1..10)                              # ✅ Range


## SECCIÓN 3: OPERADORES

# Aritméticos
suma = 100 + 200                 # ✅ Operación correcta
division = 10 / "2"              # ❌ Error semántico: división entre número y string
division_correcta = 10 / 2       # ✅ Operación correcta
modul = 10 % 2                   # ✅ Operación correcta

# Comparación
igual = 5 == 5                   # ✅ Operación correcta
comparar = "5" > 3               # ❌ Error Semántico: no se puede comparar string con número
comparar_OK = 5 > 3              # ✅ Operación correcta

# Lógicos
es_valido = true && false        # ✅ Operación correcta
error_logico = "true" || false   # ❌ Error semántico: "true" es string, no booleano

# Asignación
x = 5                            # ✅ Operación correcta
x += 3                           # ✅ Operación correcta
x /= "a"                         # ❌ Error semántico: no se puede dividir por string


## SECCIÓN 4: EXPRESIONES

# Aritméticas
total = (3 + 2) * 4 / 2             # ✅ Expresión correcta

# Booleanas
condicion = (5 > 2) && (3 < 8)      # ✅ Expresión correcta
condicion2 = (true && "false")      # ❌ Error semántico: mezcla de booleano y string


## SECCIÓN 5: ESTRUCTURAS DE CONTROL

#While
i = 0                               # ❌ Error sintáctico: falta `end` para cerrar el while
while i < 3
  puts "Iteración #{i}"
  i += 1

i = 0                               # ✅ Estructura de control correctamente definida
while i < 3
  puts "Iteración #{i}"
  i += 1
end


#if-else
imc = 20
if imc >= 25                         # ✅ Estructura de control correctamente definida
  puts "Indice de Masa Corporal Alto. Sobrepeso - Obesidad"
else
  puts "Indice de Masa Corporal Normal - Bajo."
end

if "hola"                          # ❌ Error sintáctico: "hola" es string y no es parte de IF
  puts "Activo"
end


## SECCION 6: DECLARACION DE FUNCIONES

# Función con valor por defecto
def saludo(nombre = "Usuario")       # ✅ Función correctamente declarada
  puts "Hola, #{nombre}"
end

saludo()                             # ❌ Error semántico: espera 1 argumento
saludo("Genesis")


# Función sin parámetros que retorna un String
def obtener_nombre                # ✅ Función correctamente declarada
  return "Genesis"
end
puts "El nombre es #{obtener_nombre()}"



# Función con parámetros
def imprimir(a)                # ✅ Función correctamente declarada
  puts a
end
result = imprimir(5)

def imprimir(a)                # ❌ Error sintáctico: Declaración incompleta, falta `end`
  puts a


## SECCION 7: CLASES Y OBJETOS

class Vehiculo
  def initialize(marca, modelo)
    @marca = marca
    @modelo = modelo
  end

  def descripcion
    return "Vehículo: #{@marca} #{@modelo}"
  end
end

carro = Vehiculo.new("Toyota", "Corolla")    # ✅ Creación de objeto correcta
puts carro.descripcion

objeto = Vehiculo("Mazda", "CX-5")           # ❌ Error sintáctico: falta .new para crear objeto

## SECCION 7: CONVERSION DE TIPO DE DATOS
"123".to_i
45.to_str                            # ❌ Error semántico: to_str no existe
45.to_s
"55.5".to_i
"55.5".to_f


