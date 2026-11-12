# Accept temperature in Celsius and convert it into Fahrenheit. Formula: F = (C × 9/5) + 32
# Display the result using an f-string with two decimal places.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit is {fahrenheit:.2f}")