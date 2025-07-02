# Modules in Python: Explanation and Examples

# What is a module?
# A module is a file containing Python code (functions, variables, classes, etc.) that you can import and use in other Python programs.
# Modules help you organize your code into separate files for better structure, reusability, and maintainability.

# There are three main types of modules:
# 1. Standard Library Modules (built-in, like math, random, os, sys, etc.)
# 2. Third-party Modules (installed via pip, like numpy, requests, flask, etc.)
# 3. User-defined Modules (your own .py files)

# Example 1: Importing a standard library module
import math
print(math.sqrt(16))  # Output: 4.0

# Example 2: Importing specific functions from a module
from random import randint
print(randint(1, 10))  # Output: Random integer between 1 and 10

# Example 3: Importing a user-defined module
# Suppose you have a file called mymodule.py with a function greet()
# In modules.py, you can do:
# import mymodule
# mymodule.greet("Alice")

# Or import just the function:
# from mymodule import greet
# greet("Alice")

# Why use modules?
# - To organize code into logical parts
# - To reuse code across multiple programs
# - To use code written by others (standard library or third-party)

# You can see all the names defined in a module using dir()
print(dir(math))  # Lists all functions and variables in the math module

# You can check the location of a module file
print(math.__file__)  # Shows the path to the math module (if available)

# Summary:
# - Modules are Python files you can import and use.
# - They help keep code organized and reusable.
# - Use import statements to bring modules into your program