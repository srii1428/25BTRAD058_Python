# Simple calculator and area calculation programs.

print("------ SIMPLE CALCULATOR ------")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
if b != 0:
    print("Division =", a / b)
else:
    print("Division not possible")
print("\n------ AREA OF RECTANGLE ------")
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of Rectangle =", area)