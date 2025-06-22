# SETS in Python 

# Sets in Python are a built-in data type that allows you to store an unordered collection of unique elements.
# They are similar to mathematical sets and provide various operations for manipulating collections of items.
# Sets are unordered collections of unique elements.
# They are useful for storing unique items and performing set operations like union, intersection, and difference
# Example of set operations
set1 = {1, 2, 3}  # First set
set2 = {3, 4, 5}  # Second set
# Union of two sets
union_result = set1.union(set2)  # Union operation
print("Union of Set1 and Set2:", union_result)  # Output: Union of Set1 and Set2: {1, 2, 3, 4, 5}
# Intersection of two sets
intersection_result = set1.intersection(set2)  # Intersection operation
print("Intersection of Set1 and Set2:", intersection_result)  # Output: Intersection of Set1 and Set2: {3}
# Difference of two sets
difference_result = set1.difference(set2)  # Difference operation
print("Difference of Set1 and Set2:", difference_result)  # Output: Difference of Set1 and Set2: {1, 2}
# Symmetric difference of two sets
symmetric_difference_result = set1.symmetric_difference(set2)  # Symmetric difference operation
print("Symmetric Difference of Set1 and Set2:", symmetric_difference_result)  # Output: Symmetric Difference of Set1 and Set2: {1, 2, 4, 5}

# Sets can also be used to check for membership and perform operations like adding or removing elements.
# Example of adding and removing elements in a set
set1.add(4)  # Adding an element to the set
print("Set1 after adding 4:", set1)  # Output: Set1 after adding 4: {1, 2, 3, 4}
set1.remove(2)  # Removing an element from the set
print("Set1 after removing 2:", set1)  # Output: Set1 after removing 2: {1, 3, 4}

# Sets are mutable, meaning you can modify them by adding or removing elements.
# Example of modifying a set
my_set = {1, 2, 3}  # Initial set
print("Initial Set:", my_set)  # Output: Initial Set: {1, 2, 3}

# However, the elements in a set must be immutable (like numbers, strings, or tuples).
# Sets are commonly used in scenarios where you need to store unique items or perform set operations.
# Example of using a set to store unique items
unique_items = {"apple", "banana", "cherry"}  # Set of unique items
print("Unique Items:", unique_items)  # Output: Unique Items: {'apple', 'banana', 'cherry'}
# You can add new items to the set
unique_items.add("orange")  # Adding a new item to the set
print("Unique Items after adding orange:", unique_items)  # Output: Unique Items after adding orange: {'apple', 'banana', 'cherry', 'orange'}
# You can also remove items from the set
unique_items.remove("banana")  # Removing an item from the set
print("Unique Items after removing banana:", unique_items)  # Output: Unique Items after removing banana: {'apple', 'cherry', 'orange'}

# Sets are useful for tasks like removing duplicates from a list, checking membership, and performing set
# operations like union, intersection, and difference.
# Example of using a set to remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]  # List with duplicates
unique_numbers = set(numbers)  # Converting the list to a set to remove duplicates
print("Unique Numbers from List:", unique_numbers)  # Output: Unique Numbers from List: {1, 2, 3, 4, 5}

# You can convert the set back to a list if needed
unique_numbers_list = list(unique_numbers)  # Converting the set back to a list
print("Unique Numbers as List:", unique_numbers_list)  # Output: Unique Numbers as List: [1, 2, 3, 4, 5]

# Sets are a powerful data structure in Python that allow you to store unique items and perform set operations efficiently.
# You can also use loops to iterate over the elements in a set.
for item in unique_items:
    print("Item in Unique Items:", item)  # Output: Item in Unique Items: apple, Item in Unique Items: cherry, Item in Unique Items: orange
# The loop iterates over each item in the set and prints it.

#___________________________________________________________________________
