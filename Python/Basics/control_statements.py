# Control Statements in Python

# Control statements allow you to control the flow of execution in your Python programs.

# They include conditional statements, loops, and exception handling.

# if Statements
# if statements allow you to execute a block of code based on a condition.

num = 10

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
    
#-------------------------------------------
# Some more Statements
    
# while Loops
# while loops allow you to execute a block of code repeatedly as long as a condition is true

count = 0

while count < 5:
    print("Count is:", count)
    count += 1  # Increment the count by 1
# The loop will stop when count reaches 5

# for Loops
# for loops allow you to iterate over a sequence (like a list, tuple, or string

fruits = ["apple", "banana", "cherry"]


for fruit in fruits:
    print("Fruit:", fruit)
# The loop will iterate over each fruit in the list


# break and continue Statements
# break statements allow you to exit a loop prematurely, while continue statements skip the current iteration and 
# move to the next iteration.
for i in range(5):
    if i == 2:
        print("Skipping 2")
        continue  # Skip the rest of the loop for this iteration
    if i == 4:
        print("Breaking at 4")
        break  # Exit the loop
    print("Current number:", i)
# The loop will skip printing 2 and break when it reaches 4

