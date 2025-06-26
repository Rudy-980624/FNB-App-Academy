import math

print("Scientific Calculator")
print("You can enter a mathematical expression as a string (e.g., 2 + 3 * 4, math.sin(math.pi/2), sqrt(16), etc.)")
print("Available functions: +, -, *, /, **, sqrt, sin, cos, tan, log, exp, factorial, pi, e, etc.")
print("Type 'exit' to quit.")

# Provide a safe dictionary for eval
safe_dict = {
    'sqrt': math.sqrt,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'log': math.log,
    'exp': math.exp,
    'factorial': math.factorial,
    'pi': math.pi,
    'e': math.e,
    'abs': abs,
    'pow': pow,
    '__builtins__': {}
}

while True:
    expr = input("Enter expression: ") # Input expression
    if expr.lower() == 'exit':
        print("Goodbye!")
        break
    try:
        # Evaluate the expression safely
        result = eval(expr, safe_dict)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)