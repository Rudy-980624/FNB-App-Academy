# Tuples in Pyton is a collection of ordered elements similar to lists
# However, Tuples are immutable meaning that once it has been created, elements are unchangable
# Therefore Tuples will present a fixed number of items that should not be modified 

my_tuples = (1, 2, 3, 4, 5)
print(my_tuples)

# Use Indexing to display specific element in tuple
print(my_tuples[3]) 
print(my_tuples[2])
print(my_tuples[-1]) # Use of Negative numbers wil count backwards from the end of the list 

# Other tools can still b usd with tuples 

tuple_materials = ('Cotton', 'Leather', 'Silk')
tuple_colour = ('Brown', 'Black', 'White')

conc_tuple = tuple_materials + tuple_colour # Cancatenate two tuples
print(conc_tuple)

rep_tuple = tuple_colour * 2 # Repeat tuple twice 
print(rep_tuple)