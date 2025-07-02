# Functions are a fundamental way to structure your code 
# They allow you to encapsulate a piece of code and re-use it throughout your program
# This leads to more readable and managable code

# Define the function by using the "def" key word followed by the followed by the def key-word and a perenthesis
# Inside the perenthesis ny parameters that the function should take can be specified 
# After that we have a ':' to start the indented block of code that makes up the ody of the function 

# Example 1: A simple greeting function

def greet(name):
    # This function prints a greeting to the user with the given name
    print(f'Hello {name}')
    
greet('Alice')# Calls the greet function with 'Alice' as the argument

# Example 2: A function that adds two numbers and returns the result

def add(a, b):
    # This function returns the sum of a and b
    return a + b

result = add(2, 5) # Calls the add function with 2 and 5 as arguments
print(result) # Prints the result (7)


# Functions can contain loops and various other elements that can build your structure

# Example 3: Recursive function to calculate factorial

def factorial(n):
    # This function returns the factorial of n using recursion
    # Base case: factorial(0) is 1
    if n == 0:
        return 1
    else:
        # Recursive case: n * factorial(n-1)
        return n*factorial(n-1)

# Why use recursion? 
# Recursion allows a function to call itself to solve smaller instances of the same problem.
# It's useful for problems that can be broken down into similar subproblems, like factorials, Fibonacci, etc.

    
# Example 4: Function with a default parameter value

def greet(name, greeting ="Hello"):
    # This function prints a customizable greeting.
    # If no greeting is provided, it defaults to "Hello".
    print(f"{greeting}, {name}")
    
greet('Bob', 'Good Morning')  # Prints: Good Morning, Bob
greet('Alice')                # Prints: Hello, Alice (uses default greeting)

# Why use default parameters?
# Default parameters make your functions more flexible and easier to use,
# allowing you to call them with fewer arguments when appropriate.