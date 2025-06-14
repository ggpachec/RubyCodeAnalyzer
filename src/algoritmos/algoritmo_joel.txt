def calcular_area(base, altura)
area = base * altura / 2
puts "El área es #{area}"
return area
end
base = 10
altura = 5
resultado = calcular_area(base, altura)
if resultado > 20
puts "Área grande"
else
puts "Área pequeña"
end