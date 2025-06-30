# Test algorithm for lexical, syntactic and semantic analysis

# Variables and assignments
x = 5
y = 2.5
z = "hello"
flag = true
undef_var = a + 3          # Semantic: 'a' is not defined

# Type conversion
num_str = "123"
num_int = num_str.to_i     # OK
num_float = num_str.to_f   # OK
converted = x.to_s         # OK

invalid_conv = flag.to_i   # Semantic: 'to_i' not defined for bool

# Arithmetic operations
sum = x + y
diff = x - y
prod = x * 2
div = y / 2
power = x ** 2
modulo = x % 2

str_sum = z + x            # Semantic: can't add string and int

# Compound assignment
x += 1
z += " world"              # Semantic: can't add string and int (in this context)

# Arrays, hashes, ranges
arr = [1, 2, 3]
h = { "one": 1, "two": 2 }
rng = (1..5)

# Print and input
puts "Enter value:"
input_val = gets.chomp

# Functions
def my_sum(a, b)
  return a + b
end

def greet(name = "User")
  puts "Hello, #{name}"
  return 42              # Semantic: return type int, but should be string
end

val1 = my_sum(x, y)
greet("Alice")

# Class and method
class Person
  def initialize(name, age)
    @name = name
    @age = age
  end

  def show
    puts "Name: #{@name}, Age: #{@age}"
  end
end

p = Person.new("Tom", 20)
p.show

# Control structures
if flag
  puts "Flag is true"
end

if z                 # Semantic: IF with string condition
  puts "z is truthy"
end

while x > 0
  puts x
  x -= 1
end

while "loop"         # Semantic: WHILE with string condition
  break              # OK, inside loop
end

break                # Semantic: break outside loop

for i in 1..3
  puts i
end

# Logical operations
result = flag && false
result2 = flag || z     # Semantic: OR with non-bool operand

# Comparison
eq = x == z             # Semantic: comparison between int and string
neq = arr != h          # Semantic: comparison between array and hash

# Multi-line comment
=begin
This is a multi-line comment
=end

# End of test algorithm


