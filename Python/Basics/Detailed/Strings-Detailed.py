# Strings are immutable sequences of Unicode characters.
# They can be created using single quotes, double quotes, or triple quotes for multi-line strings
# Example of creating strings
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_quote_string = """This is a multi-line string.It can span multiple lines."""

# Strings can be concatenated using the + operator
concatenated_string = single_quote_string + " " + double_quote_string
# output: 'Hello, World! Hello, World!'

# Strings can be repeated using the * operator
repeated_string = single_quote_string * 3
# output: 'Hello, World!Hello, World!Hello, World!'

# Strings can be indexed and sliced
first_character = single_quote_string[0]  # 'H'
last_character = single_quote_string[-1]  # '!'
substring = single_quote_string[0:5]  # 'Hello'
# output: 'Hello'

# Strings can be iterated over
for char in single_quote_string:
    print(char, end=' ')  # Prints each character in the string
# output: # H e l l o ,   W o r l d !

# Strings can be formatted using f-strings (Python 3.6+)
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
# output: 'My name is Alice and I am 30 years old.'

# Strings can be formatted using the format() method
formatted_string_method = "My name is {} and I am {} years old.".format(name, age)
# output: 'My name is Alice and I am 30 years old.'

# Strings can be split into a list of substrings
split_string = single_quote_string.split(", ")  # ['Hello', 'World!']
# output: ['Hello', 'World!']

# Strings can be joined using the join() method
joined_string = ", ".join(split_string)  # 'Hello, World!'
# output: 'Hello, World!'

# Strings can be stripped of leading and trailing whitespace
stripped_string = "   Hello, World!   ".strip()  # 'Hello, World!'
# output: 'Hello, World!'

# Strings can be checked for membership using the 'in' operator
is_member = "Hello" in single_quote_string  # True
# output: True

# Strings can be checked for equality
is_equal = single_quote_string == double_quote_string  # True
# output: True

# Strings can be converted to uppercase or lowercase
uppercase_string = single_quote_string.upper()  # 'HELLO, WORLD!'
lowercase_string = single_quote_string.lower()  # 'hello, world!'
# output: 'HELLO, WORLD!', 'hello, world!'

# Strings can be checked for alphanumeric characters
is_alphanumeric = single_quote_string.isalnum()  # False (contains punctuation)
# output: False

# Strings can be checked for alphabetic characters
is_alpha = single_quote_string.isalpha()  # False (contains punctuation and space)
# output: False

# Strings can be checked for numeric characters
is_numeric = single_quote_string.isnumeric()  # False (contains letters and punctuation)
# output: False

# Strings can be checked for digits
is_digit = single_quote_string.isdigit()  # False (contains letters and punctuation)
# output: False

# Strings can be checked for whitespace
is_space = single_quote_string.isspace()  # False (contains letters and punctuation)
# output: False

# Strings can be checked for title case
is_title = single_quote_string.istitle()  # True (first letter of each word is uppercase)
# output: True

# Strings can be checked for uppercase
is_upper = single_quote_string.isupper()  # False (not all letters are uppercase)
# output: False

# Strings can be checked for lowercase
is_lower = single_quote_string.islower()  # False (not all letters are lowercase)
# output: False

# Strings can be checked for a specific prefix or suffix
has_prefix = single_quote_string.startswith("Hello")  # True
has_suffix = single_quote_string.endswith("World!")  # True
# output: True, True

# Strings can be replaced using the replace() method
replaced_string = single_quote_string.replace("World", "Python")  # 'Hello, Python!'
# output: 'Hello, Python!'

# Strings can be counted for occurrences of a substring
count_substring = single_quote_string.count("o")  # 2
# output: 2

# Strings can be found using the find() method
find_index = single_quote_string.find("World")  # 7
# output: 7

# Strings can be checked for the presence of a substring using the 'in' operator    
contains_substring = "World" in single_quote_string  # True
# output: True

# Strings can be reversed using slicing
reversed_string = single_quote_string[::-1]  # '!dlroW ,olleH'
# output: '!dlroW ,olleH'

# Strings can be converted to a list of characters
list_of_characters = list(single_quote_string)  # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
# output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# Strings can be converted to a tuple of characters
tuple_of_characters = tuple(single_quote_string)  # ('H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!')
# output: ('H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!')

# Strings can be checked for the presence of a substring using the 'index' method
index_substring = single_quote_string.index("World")  # 7
# output: 7

# Strings can be checked for the presence of a substring using the 'rfind' method
rfind_substring = single_quote_string.rfind("o")  # 8
# output: 8

# Strings can be checked for the presence of a substring using the 'rindex' method
rindex_substring = single_quote_string.rindex("o")  # 8
# output: 8

# Strings can be capitalized
capitalized_string = single_quote_string.capitalize()  # 'Hello, world!'
# output: 'Hello, world!'

# Strings can be converted to title case
title_string = single_quote_string.title()  # 'Hello, World!'
# output: 'Hello, World!'

# Strings can be swapcased
swapcase_string = single_quote_string.swapcase()  # 'hELLO, wORLD!'
# output: 'hELLO, wORLD!'

# Strings can be zero-filled
zfilled_string = single_quote_string.zfill(20)  # '0000000Hello, World!'
# output: '0000000Hello, World!'

# Strings can expand tabs
expandtabs_string = "Hello\tWorld".expandtabs(4)  # 'Hello   World'
# output: 'Hello   World'

# Strings can be translated
translation_table = str.maketrans("aeiou", "12345")  # Create a translation table
translated_string = single_quote_string.translate(translation_table)  # 'H2ll4, W4rld!'
# output: 'H2ll4, W4rld!'

# Strings can have prefixes and suffixes removed (Python 3.9+)
removeprefix_string = single_quote_string.removeprefix("Hello, ")  #'World!'
removesuffix_string = single_quote_string.removesuffix(" World!")  # 'Hello,'
# output: 'World!', 'Hello,'

# Strings can be casefolded
casefolded_string = single_quote_string.casefold()  # 'hello, world!'
# output: 'hello, world!'

# Strings can use format_map
format_map_string = "My name is {name} and I am {age} years old.".format_map({'name': name, 'age': age})
# output: 'My name is Alice and I am 30 years old.'

# Strings can be partitioned
partitioned_string = single_quote_string.partition(", ")  # ('Hello', ', ', 'World!')
# output: ('Hello', ', ', 'World!')

# Strings can be rpartitioned
rpartitioned_string = single_quote_string.rpartition(", ")  # ('Hello', ', ', 'World!')
# output: ('Hello', ', ', 'World!')

# Strings can be split into lines
splitlines_string = """Hello, World!This is a multi-line string.""".splitlines()
# output: ['Hello, World!', '', 'This is a multi-line string.']

# Strings can be right-split
rsplit_string = single_quote_string.rsplit(", ")  # ['Hello', 'World!']
# output: ['Hello', 'World!']

# Strings can be centered, left-justified, or right-justified
centered_string = single_quote_string.center(20, '-')  # '----Hello, World!----'
ljusted_string = single_quote_string.ljust(20, '-')  # 'Hello, World!-----'
rjusted_string = single_quote_string.rjust(20, '-')  # '-----Hello, World!'
# output: '----Hello, World!----', 'Hello, World!-----', '-----Hello, World!'

