# Write a program to prime number and factorial programs.
# B. Factorial

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
    print("Factorial =", factorial)