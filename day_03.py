### Boolean ###
# A boolean data type represent one of the two values: True or False. This is dat type so important in comparisson operator.

### Operator ###
# Assignment Operator are =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=

# Arithmetic Operators are +, -, *, /, %, //, **

# Example of Integers, Float, and Complex number
print('Addition:', 1 + 2)
print('Subtraction:', 2 - 1)
print('Multiplication:', 3 * 2)
print('Division:', 4 / 2)   # Note division in Python always give floating number
print('Division without the remainder', 7 // 3)     # Note this is like modulus and not give floating number
print('Division without the remainder', 6 // 3)
print('Modulus', 3 % 2)
print('Exponentiation:', 2 ** 4)
print('Floating point number, PI', 3.14)
print('Floating point number, gravity', 9.81)
print('Complex Number', 1 + 1j)
print('Multiplying complex numbers:', (1 + 1j) * (1 - 1j))

# Declaring variable and do operations with that variables
num_one = 3
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_one / num_two
remainder = num_two % num_one

print('total', total)
print('diff', diff)
print('product', product)
print('div', div)
print('remainder', remainder)

# Comparison Operators are ==, !=, >, <, >=, <=
print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 <= 3)
print(2 == 3)
print(3 != 3)

# Another comparison are is, is not, in, not in
print('1 is 1', 1 is 1)
print('1 is not 1', 1 is not 1)
print('1 is not 2', 1 is not 2)
print('A in Asabeneh', 'A' in 'Asabeneh')
print('B not in Asabeneh', 'B' not in 'Asabeneh')

# Logical operator are and, or, not
print(3 > 2 and 4 > 3)
print(3 > 2 and 4 < 3)
print(3 > 2 or 4 > 3)
print(3 > 2 or 4 < 3)
print(not 3 > 2)    # Note will return False if the result true/correct and otherwise
print(not not True) # True
print(not not False) #False

### Exercise ###
age = 25
height = 161.0
complex = 2 + 4j
base = float(input('Enter base:'))
height = float(input('Enter height:'))
areaTriangle = height * base / 2
print('Area of triangle is', areaTriangle)
side_a = float(input('Enter side a:'))
side_b = float(input('Enter side b:'))
side_c = float(input('Enter side c:'))
perimeterTriangle = side_a + side_b + side_c
print('Perimeter of triangle is', perimeterTriangle)
length = float(input('Enter length:'))
width = float(input('Enter width:'))
perimeterRectagle = 2 * (length + width)
print('Perimeter of rectagle is', perimeterRectagle)
radius = float(input('Enter radius:'))
areaCircle = 3.14 * radius ** 2
cicumference = 2 * 3.14 * radius
print('Area Circle is', areaCircle)
print('Circumference is', cicumference)
#y = 2x - 2
slope = 2
y_intercept = -2
x_intercept = (0 - y_intercept) / slope
print('x-intercept is', x_intercept)