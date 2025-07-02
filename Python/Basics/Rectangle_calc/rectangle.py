# rectangle.py - Rectangle Area and Perimeter Calculator using a Module

# Import the calc module (user-defined module that contains area and perimeter functions)
import calc

# Prompt the user to enter the rectangle's length and width
length = float(input('Enter rectangle length: '))
width = float(input('Enter rectangle Width: '))

# Calculate the area using the area() function from the calc module
area = calc.area(length, width)

# Calculate the perimeter using the permeter() function from the calc module
perimeter = calc.permeter(length, width)

# Display the results to the user
print(f'Rectangle Area = {area}')
print(f'Rectangle Perimeter = {perimeter}')

# --- Explanation and Reasons ---

# Why use a module (calc)?
# - Separates calculation logic from user interaction, making code easier to maintain and reuse.
# - If you need to use area or perimeter calculations elsewhere, you can simply import calc.
# - Keeps your main script clean and focused on input/output.

# Why use functions for area and perimeter?
# - Functions encapsulate logic, making your code modular and testable.
# - If the formula changes, you only need to update it in one place (the calc module).