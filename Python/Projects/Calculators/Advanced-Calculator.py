import math # import math for mathematical operations

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power (x^y)")
print("6. Square Root")
print("7. Factorial")

operation = int(input("Enter operation (1/2/3/4/5/6/7): ")) # Input operation choice

if operation in (1, 2, 3, 4, 5): # Basic arithmetic operations
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if operation == 1: # Addition
        print(f"{x} + {y} = {x + y}")
    elif operation == 2: # Subtraction
        print(f"{x} - {y} = {x - y}")
    elif operation == 3: # Multiplication
        print(f"{x} * {y} = {x * y}")
    elif operation == 4: # Division
        if y == 0:
            print("Error: Division by zero")
        else:
            print(f"{x} / {y} = {x / y}")
    elif operation == 5: # Power
        print(f"{x} ^ {y} = {x ** y}")

elif operation == 6: # Square Root
    x = float(input("Enter number: "))
    if x < 0:
        print("Error: Cannot take square root of a negative number")
    else:
        print(f"√{x} = {math.sqrt(x)}")

elif operation == 7: # Factorial
    x = float(input("Enter number: "))
    if x < 0 or not x.is_integer():
        print("Error: Factorial only defined for non-negative integers")
    else:
        print(f"{int(x)}! = {math.factorial(int(x))}")

else:
    print("Invalid operation")

print("Quick Maths!!!")
# This code extends the original calculator to include power, square root, and factorial operations.