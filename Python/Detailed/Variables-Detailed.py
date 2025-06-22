# Variables are used to store data in Python. They can hold different types of values, such as numbers, strings, lists, and more.
# Example of variable assignment
name = "Alice"  # String variable
age = 30        # Integer variable
height = 5.5   # Float variable
# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)

# Variables can be reassigned to different values
age = 31  # Reassigning the age variable
print("Updated Age:", age)

# Variables can also hold collections of data, such as lists
fruits = ["apple", "banana", "cherry"]  # List variable
# Accessing elements in a list
print("First fruit:", fruits[0])  # Accessing the first element
# Adding a new fruit to the list
fruits.append("orange")
print("Updated fruits list:", fruits)  # Printing the updated list

# Variables can also be used in expressions
total_age = age + 5  # Adding 5 to the current age
print("Total age after 5 years:", total_age)  # Printing the result of the expression

# Variables can be used in functions
def greet(person_name):
    return f"Hello, {person_name}!"
# Calling the function with a variable
greeting = greet(name)
print(greeting)  # Printing the greeting message

# Variables can also be used to store boolean values
is_student = True  # Boolean variable
print("Is student:", is_student)  # Printing the boolean value

# Variables can be used in conditional statements
if is_student:
    print(f"{name} is a student.")
else:
    print(f"{name} is not a student.")

# Variables can also be used to store dictionaries
person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}  # Dictionary variable
# Accessing values in a dictionary
print("Person Info:", person_info)  # Printing the entire dictionary
# Accessing a specific value in the dictionary
print("Person's Name:", person_info["name"])  # Accessing the name from the
# dictionary

# Variables can be used in loops
for fruit in fruits:
    print("Fruit:", fruit)  # Printing each fruit in the list

# Variables can also be used to store tuples
coordinates = (10.0, 20.0)  # Tuple variable
# Accessing elements in a tuple
print("Coordinates:", coordinates)  # Printing the entire tuple
# Accessing a specific element in the tuple
print("X Coordinate:", coordinates[0])  # Accessing the first element (X coordinate
print("Y Coordinate:", coordinates[1])  # Accessing the second element (Y coordinate)

# Variables can be used to store sets
unique_numbers = {1, 2, 3, 4, 5}  # Set variable
# Printing the set
print("Unique Numbers:", unique_numbers)  # Printing the entire set
# Adding a new number to the set
unique_numbers.add(6)
print("Updated Unique Numbers:", unique_numbers)  # Printing the updated set

# Variables can also be used to store None values
no_value = None  # None variable
# Printing the None value
print("No Value:", no_value)  # Printing the None value
# Checking if a variable is None
if no_value is None:
    print("The variable 'no_value' is None.")
else:
    print("The variable 'no_value' has a value.")
# Variables can be used to store functions

def add_numbers(x, y):
    return x + y  # Function to add two numbers
# Storing the function in a variable
add_func = add_numbers  # Assigning the function to a variable
# Calling the function using the variable
result = add_func(5, 10)  # Calling the function with arguments
print("Result of adding 5 and 10:", result)  # Printing the result of the function call

# Variables can also be used to store classes
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable for name
        self.age = age    # Instance variable for age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
# Creating an instance of the Person class
person_instance = Person(name, age)  # Creating a new Person object
# Calling the introduce method of the Person instance
introduction = person_instance.introduce()  # Calling the method to get the introduction
print(introduction)  # Printing the introduction message

# Variables can also be used to store modules
import math  # Importing the math module
# Using a variable to store a function from the math module
sqrt_func = math.sqrt  # Assigning the square root function to a variable
# Calling the square root function using the variable
sqrt_result = sqrt_func(16)  # Calculating the square root of 16
print("Square root of 16:", sqrt_result)  # Printing the result of the square
# root calculation

# Variables can be used to store file paths
file_path = "data.txt"  # String variable for file path
# Printing the file path
print("File Path:", file_path)  # Printing the file path variable
# Variables can also be used to store URLs
url = "https://www.example.com"  # String variable for URL
# Printing the URL
print("URL:", url)  # Printing the URL variable

# Variables can be used to store configuration settings
config = {
    "debug": True,
    "version": "1.0.0",
    "max_users": 100
}  # Dictionary variable for configuration settings
# Printing the configuration settings
print("Configuration Settings:", config)  # Printing the entire configuration dictionary
# Accessing a specific configuration setting
print("Debug Mode:", config["debug"])  # Accessing the debug setting from the configuration
# Accessing the version setting from the configuration
print("Version:", config["version"])  # Accessing the version setting from the configuration
# Accessing the max_users setting from the configuration
print("Max Users:", config["max_users"])  # Accessing the max_users setting from the configuration

# Variables can also be used to store environment variables
import os  # Importing the os module to access environment variables
# Getting an environment variable
home_directory = os.getenv("HOME")  # Getting the HOME environment variable
# Printing the home directory
print("Home Directory:", home_directory)  # Printing the home directory variable
# Setting an environment variable
os.environ["MY_VARIABLE"] = "Hello, World!"  # Setting a new environment variable
# Getting the newly set environment variable
my_variable = os.getenv("MY_VARIABLE")  # Getting the value of the new environment variable
# Printing the value of the new environment variable
print("My Variable:", my_variable)  # Printing the value of the new environment variable

# Variables can also be used to store command-line arguments
import sys  # Importing the sys module to access command-line arguments
# Checking if command-line arguments are provided
if len(sys.argv) > 1:
    command_line_arg = sys.argv[1]  # Getting the first command-line argument
    print("Command-Line Argument:", command_line_arg)  # Printing the command-line argument
else:
    print("No command-line arguments provided.") # Printing a message if no command-line arguments are provided
    
# Variables can also be used to store JSON data
import json  # Importing the json module to work with JSON data
# Example JSON data as a string
json_data = '{"name": "Bob", "age": 25, "city": "New York"}'  # JSON string
# Parsing the JSON data into a Python dictionary
parsed_data = json.loads(json_data)  # Converting JSON string to Python dictionary
# Printing the parsed JSON data
print("Parsed JSON Data:", parsed_data)  # Printing the entire parsed dictionary
# Accessing a specific value in the parsed JSON data
print("Name from JSON Data:", parsed_data["name"])  # Accessing the name from the parsed JSON data
# Accessing the age from the parsed JSON data
print("Age from JSON Data:", parsed_data["age"])  # Accessing the age from the parsed JSON data
# Accessing the city from the parsed JSON data
print("City from JSON Data:", parsed_data["city"])  # Accessing the city from the parsed JSON data

# Variables can also be used to store XML data
import xml.etree.ElementTree as ET  # Importing the ElementTree module to work with XML data
# Example XML data as a string
xml_data = '''<person>
    <name>Charlie</name>
    <age>28</age>
    <city>Los Angeles</city>
    </person>'''  # XML string
# Parsing the XML data into an ElementTree object
root = ET.fromstring(xml_data)  # Converting XML string to ElementTree object
# Printing the root element of the XML data
print("Root Element:", root.tag)  # Printing the tag of the root element
# Accessing specific elements in the XML data
name_element = root.find("name")  # Finding the name element

#_____________________________________________________________________________________

