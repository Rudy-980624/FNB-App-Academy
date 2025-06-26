# Sets in Python an unordered st of unique elements
# Unlike lists or tuples, sets do not allow duplicat values
# sets are useful to perform operations like union and intersection as well as the difference between diffrence betwen collection of elements 

# Sets are unordered and imutable but can add an remove and do not allow duplicates 
'''
my_set = {1, 2, 4, 5, 6} # Declared set
print(my_set)

my_set.add(7) # Add value to set
print(my_set)

my_set.remove(2) # Remove value from set
print(my_set)
#--------------------------------------------------
'''
set1 = {4, 5, 6, 7, 8, 9}
set2 = {1, 2, 4, 5, 6, 7}

# Union combines both sets together and removes duplicated data

union_set = set1.union(set2) # Declare new value of unionized sets
print(union_set)

# Intrsection identifies values that are the same

inter_set = set1.intersection(set2) # declare new interset variable, intrsecting set1 and set2
print(inter_set) # Prints values that are the same from both sets

# Difference identifies values that are not the same  

diff_set = set1.difference(set2) # Declare new diffrence variable, deffering set1 and set2
print(diff_set) # prints valus that are deifferent from both sets