# Advanced Python Functions: Examples, Notes, and Explanations

# 1. Function with Arbitrary Positional Arguments (*args)
def sum_all(*args):
    """
    Accepts any number of positional arguments and returns their sum.
    *args collects arguments into a tuple.
    """
    return sum(args)

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(5, 10, 15, 20))  # Output: 50

# Why use *args?
# Use *args when you want your function to accept any number of positional arguments.

# 2. Function with Arbitrary Keyword Arguments (**kwargs)
def print_info(**kwargs):
    """
    Accepts any number of keyword arguments and prints them as key-value pairs.
    **kwargs collects arguments into a dictionary.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

# Why use **kwargs?
# Use **kwargs when you want your function to accept any number of named (keyword) arguments.

# 3. Lambda (Anonymous) Functions
multiply = lambda x, y: x * y
print(multiply(4, 5))  # Output: 20

# Why use lambda?
# Lambda functions are useful for short, throwaway functions, especially as arguments to higher-order functions.

# 4. Functions as Arguments (Higher-Order Functions)
def apply_function(func, value):
    """
    Takes a function and a value, and applies the function to the value.
    """
    return func(value)

print(apply_function(abs, -10))  # Output: 10

# Why use functions as arguments?
# This allows for flexible, reusable code and is the basis for functional programming patterns.

# 5. Nested Functions (Closures)
def outer(msg):
    """
    Outer function defines a message and returns an inner function that prints it.
    """
    def inner():
        print(f"Message: {msg}")
    return inner

my_func = outer("Hello from closure!")
my_func()  # Output: Message: Hello from closure!

# Why use closures?
# Closures allow inner functions to remember the state of their enclosing scope, useful for data hiding and decorators.

# 6. Decorators
def my_decorator(func):
    """
    A simple decorator that prints before and after the function call.
    """
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Bob")
# Output:
# Before function call
# Hello, Bob!
# After function call

# Why use decorators?
# Decorators allow you to add functionality to existing functions in a clean, readable way.

# 7. Type Hints in Functions (Python 3.5+)
def add_numbers(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    Type hints help with code readability and static analysis.
    """
    return a + b

print(add_numbers(3, 7))  # Output: 10

# Why use type hints?
# Type hints improve code clarity and help tools catch bugs before runtime.

# 8. Generator Functions (yield)
def countdown(n):
    """
    A generator that counts down from n to 1.
    """
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number, end=' ')  # Output: 5 4 3 2 1

# Why use generators?
# Generators are memory-efficient for large sequences and allow lazy evaluation.

# 9. Function Docstrings
def square(x):
    """
    Returns the square of x.
    This is a docstring, which documents the function.
    """
    return x * x

print(square.__doc__)

# Why use docstrings?
# Docstrings provide built-in documentation for your functions, accessible via help() and IDEs.

# 10. Keyword-Only Arguments (Python 3+)
def area(*, width, height):
    """
    Forces width and height to be specified as keyword arguments.
    """
    return width * height

print(area(width=5, height=10))  # Output: 50
# area(5, 10)  # This would raise a TypeError

# Why use keyword-only arguments?
# They improve code readability and prevent argument order mistakes.