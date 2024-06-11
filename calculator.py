# Simple calculator using if-else statements

# Get user inputs
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter first number: "))

# Perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else: result = "Error! Division by zero"
else:
    print("Error! N/A")

print(f"The result is {result}")

