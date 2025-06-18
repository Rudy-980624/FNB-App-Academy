# Operators and Strings

str1 = "Hello"
str2 = "World"

# Concatenation
result = str1 + " " + str2
print(result)  # Output: Hello World

# Repetition
result = str1 * 3
print(result)  # Output: HelloHelloHello

#------------------------------------------------------
# Other String Operations

# String Length
length = len(str1)
print(length)  # Output: 5

# String Comparison
is_equal = str1 == str2
print(is_equal)  # Output: False

# String Membership
is_in = "Hello" in result
print(is_in)  # Output: True

# String Slicing
sliced = result[0:5]
print(sliced)  # Output: Hello

# String Formatting
formatted = f"{str1}, {str2}!"
print(formatted)  # Output: Hello, World!

# String Methods
upper_str = str1.upper()
print(upper_str)  # Output: HELLO
lower_str = str2.lower()
print(lower_str)  # Output: world

# String Replacement
replaced = result.replace("World", "Python")
print(replaced)  # Output: Hello Python

# String Splitting
split_str = result.split(" ")
print(split_str)  # Output: ['Hello', 'World']  

# String Joining
joined_str = " ".join(split_str)
print(joined_str)  # Output: Hello World

# String Stripping
stripped_str = "   Hello World!   ".strip()
print(stripped_str)  # Output: Hello World!
# String Finding
index = result.find("World")
print(index)  # Output: 6
# String Counting
count = result.count("o")
print(count)  # Output: 2
# String Reversing
reversed_str = result[::-1]
print(reversed_str)  # Output: dlroW olleH
# String Capitalization
capitalized_str = str1.capitalize()
print(capitalized_str)  # Output: Hello
# String Title Casing
title_cased_str = result.title()
print(title_cased_str)  # Output: Hello World
# String Checking
is_alpha = str1.isalpha()