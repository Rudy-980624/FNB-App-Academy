#strings

# This is a single line string
message1 = "Hello, World!"

print(message1)

# This is a multi line string 
message2 = """Python is fun! 
And awesome to learn!""" # Triple quotes allow for multi-line strings

print(message2)

# Advanced string comcepts

message3 = "Python, is fun!"

print(message3[0])  # First character
print(message3[1])  # Second character 

print(message3[-1])  # Last character
print(message3[-2])  # Second last character

print(len(message3))  # Length of the string

print(message3.strip())  # Remove whitespace from both ends
print(message3.lower())  # Convert to lowercase
print(message3.upper())  # Convert to uppercase
print(message3.split(','))  # Split the string by comma

print(message3.replace("fun", "awesome"))  # Replace a substring
print(message3.find("fun"))  # Find the index of a substring
print(message3.count("fun"))  # Count occurrences of a substring

