# Lists are used to 

fruits = ["apple", "banana", "cherry"] # List that contains 3 strings
print(fruits[0])

fruits[1] = "blueberry" # Changes the object in the list

print(fruits) # Print list with altercations made (banana = blueberry)

# Use append method to add object to end of the list

cars = ["Audi", "BMW", "Chrysler"]

cars.append("Datsun") # Append list, Add object
print(cars)

cars.insert(1, "Alpha") # Insert object into position 1 of list 
print(cars)

cars.remove("Chrysler") # Remove item from list 
print(cars)

cars.sort() # Sorts the list in assending order
print(cars)

cars.sort(reverse=True) # Sorts the list in decending order
print(cars)

