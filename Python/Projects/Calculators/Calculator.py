x = (int(input("Enter first number: "))) # Input first number
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = int(input("Enter operation (1/2/3/4): ")) # Input operation choice
y = (int(input("Enter second number: "))) # Input second number
if operation == 1:
    print(f"{x} + {y} = {x + y}") # Addition
elif operation == 2:
    print(f"{x} - {y} = {x - y}") # Subtraction
elif operation == 3:
    print(f"{x} * {y} = {x * y}") # Multiplication
elif operation == 4:
    if y == 0:
        print("Error: Division by zero")
    else:
        print(f"{x} / {y} = {x / y}") # Division
else:
    print("Invalid operation")
    
print("Quick Maths!!!")