# Exception handling 
# Exceptions are events that occur during the execution of a program 
# which disrupt the normal flow of the program's execution.

# The 'try' and 'except' blocks help to handle these situations 
# so your program can continue running or fail gracefully.

# The 'try' block contains code that may raise an exception.
# The 'except' block contains code that will execute if an exception occurs.

try:
    print(x)  # This will raise a NameError because x is not defined
except NameError:
    print('X has not been defined')  # This block handles the specific NameError
except:
    print('An Exception occurred')   # This block handles any other exception

# Why use specific exceptions (like NameError)?
# - It allows you to handle different error types in different ways.
# - More precise error handling makes debugging and maintenance easier.

# The 'finally' block can also be used.
# The 'finally' block is an optional block that can be used with the 'try' block.
# The code within the 'finally' block will be executed regardless of whether an exception occurred or not.

try:
    print(y)  # This will raise a NameError because y is not defined
except:
    print('Something went wrong...')  # Handles any exception
finally:
    print('The "Try Except" is finished...')  # This will always execute

# Why use 'finally'?
# - To ensure that certain cleanup code runs no matter what (e.g., closing files, releasing resources).
# - Guarantees that important steps are not skipped, even if an error occurs.