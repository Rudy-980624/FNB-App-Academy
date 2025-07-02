# The 'else' block
# The 'else' block in exception handling will execute only if no exceptions have been raised during the execution of the try block.
# This is useful for code that should only run if the try block was successful.

try:
    print(x)  # This will raise a NameError because x is not defined
except NameError:
    print('Undefined Variable...')  # Handles the specific NameError
else:
    print('Everything went wrong...')  # This will only run if no exception occurs in the try block

# Why use the 'else' block?
# - Keeps code that should only run when no exception occurs separate from the try block.
# - Improves readability and structure of your exception handling.

# Example of raising your own exceptions
x = -1

if x < 0:
    raise Exception('No Negative Numbers!!!')  # Raises a custom exception if x is negative

# Why raise your own exceptions?
# - Allows you to enforce rules and constraints in your code.
# - Makes your code more robust and easier to debug by providing clear error messages.