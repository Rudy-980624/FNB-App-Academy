# Loop Control Statements

# Loop control statements allow you to modify the behavior of loops in Python.
# They include `break`, `continue`, and `pass`.

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break  # Exit the loop when "cherry" is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        continue  # Skip the rest of the loop for "cherry"
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        pass  # Placeholder Do nothing for "cherry"
    print(fruit)    
    
#----------------------------------------------------------

count = 0
while count < 5:
    print(count)
    count += 1  # Increment the count by 1
    if count == 3:
        break  # Exit the loop when count reaches 3