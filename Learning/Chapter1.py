# Sub Chapter : Print function and print the line 
print(f"Hii i am an Anonymous Ethical Hacker ")
print(f"My name is Agent Badger 09")

# Sub Chapter : Variables and Data Types 
""" What is a Variable?
A variable is a container that stores data. Think of it like a labeled box where you put information. """
name = "Agent Badger 09"
age = 21

# This is the basic example of variable 
# Core Data Types in Python 
# String Data Type - "str" -Text data 

name = "Commissioner Gordan"
age = 45
city = 'UK'
sentence = "He is into the lead to investigate the crime in the website hacking case"
print(name + " is " + str(age) + " years old and lives in " + city + ". " + sentence)
print(type(name))

# Integer Data Type - "int" - Whole numbers
age = 21
year = 2026
negative_number = -5
print(age, year, negative_number)
print(type(age))

# Float Data Type - "float" - Decimal numbers
pi = 3.14159
temperature = 36.6
prize = 99.99
print(pi, temperature, prize)
print(type(pi))

#Boolean Data Type - "bool" - True or false values 
is_hacker = True
is_caught = False
print(is_hacker , is_caught)
print(type(is_hacker))

#None Data Type - "None" - Represents the absence of a value 
hacker_aliance = None 
print(type(hacker_aliance))

# Type conversion - Converting one data type into another 
age =21 
age_str = str(age)  # Convert integer to string 
print("My age is " + age_str)
print(type(age_str))

prize = 99.99
prize_int = int(prize)
print("The prize is " + str(prize_int))
print(type(prize_int))

name = "Agent Badger 09"
name_length = len(name)
print("The length of the name is " + str(name_length))

year = 2026
year_str = str(year)
print("The year is " + year_str)

# We can assign multiple variables in one line
name , age , city , proffession = "Badger09" , 21 , "UK" , "Ethical Hacker"
print(name , age , city , proffession)

# assigning the same value to multiple variables 
x = y = z = 100
print(x , y , z)

# Variable naming rules and conventions
# 1. Variable names must start with a letter or an underscore (_).
# 2. Variable names can only contain letters, numbers, and underscores.
# 3. Variable names are case-sensitive (e.g., age and Age are different variables
# 4. Variable names should not be a reserved keyword in Python (e.g., if, else, while, etc.)
# 5. Variable names should be descriptive and meaningful to improve code readability.

# Examples of valid variable names
first_name = "John"
last_name = "Doe"
age = 30
is_student = True
# Examples of invalid variable names
# 1name = "John"  # Starts with a number
# last-name = "Doe"  # Contains a hyphen
# is student = True  # Contains a space
# if = 10  # 'if' is a reserved keyword

# Best practices for variable naming
# 1. Use descriptive names that clearly indicate the purpose of the variable.
# 2. Use lowercase letters and separate words with underscores (snake_case) for variable names
# 3. Avoid using single-letter variable names except for loop counters (e.g., i, j, k).
# 4. Be consistent with your naming conventions throughout your code.
# 5. Avoid using reserved keywords as variable names to prevent syntax errors.

# Examples of good variable names
user_name = "Alice"
user_age = 25
is_logged_in = True
# Examples of bad variable names
x = "Alice"  # Not descriptive
y = 25  # Not descriptive
z = True  # Not descriptive

# In Python, you can also use underscores to create more readable variable names, especially when they consist of multiple words. This is known as snake_case. For example:
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# You can also use camelCase for variable names, which is common in other programming languages. However, snake_case is more widely used in Python. For example:
firstName = "John"
lastName = "Doe"
fullName = firstName + " " + lastName
print(fullName)

# In Python, you can also use underscores to indicate that a variable is intended for internal use (e.g., _internal_variable) or to indicate that a variable is a constant (e.g., CONSTANT_VARIABLE). However, these are just conventions and do not enforce any restrictions on the variable's usage.
_internal_variable = "This is for internal use only"
CONSTANT_VARIABLE = "This value should not change"
print(_internal_variable)
print(CONSTANT_VARIABLE)

# In Python, you can also use the built-in function `type()` to check the data type of a variable. For example:
name = "Alice"
age = 25
is_student = True
print(type(name))  # Output: <class 'str'>
print(type(age))  # Output: <class 'int'>
print(type(is_student))  # Output: <class 'bool'>

# In Python, you can also use the `input()` function to get user input and store it in a variable. For example:
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")

# In Python, you can also use the `len()` function to get the length of a string or a list. For example:
name = "Alice"
print(len(name))  # Output: 5
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

# In Python, you can also use the `str()`, `int()`, and `float()` functions to convert between different data types. For example:
age = 25
age_str = str(age)  # Convert integer to string
print("My age is " + age_str)  # Output: My age is 25
pi = 3.14159
pi_int = int(pi)  # Convert float to integer
print(pi_int)  # Output: 3

# In Python, you can also use the `isinstance()` function to check if a variable is of a certain data type. For example:
name = "Alice"
age = 25
is_student = True
print(isinstance(name, str))  # Output: True
print(isinstance(age, int))  # Output: True
print(isinstance(is_student, bool))  # Output: True

# In Python, you can also use the `del` statement to delete a variable. For example:
name = "Alice"
print(name)  # Output: Alice
del name
# print(name)  # This will raise a NameError since the variable has been deleted

# In Python, you can also use the `globals()` function to get a dictionary of all global variables in the current scope. For example:
x = 10
y = 20
print(globals())  # Output: {'x': 10, 'y': 20

# Arithematic Operations 
a = 10
b = 5
# Addition
sum = a + b
print("The sum of a and b is: " + str(sum))
# Subtraction
difference = a - b
print("The difference of a and b is: " + str(difference))
# Multiplication
product = a * b
print("The product of a and b is: " + str(product))
# Division
quotient = a / b
print("The quotient of a and b is: " + str(quotient))
# Modulus
remainder = a % b
print("The remainder of a divided by b is: " + str(remainder))
# Exponentiation
power = a ** b
print("The result of a raised to the power of b is: " + str(power))
# Floor Division
floor_division = a // b
print("The result of floor division of a by b is: " + str(floor_division))

# In Python, you can also use parentheses to control the order of operations in arithmetic expressions. For example:
result = (a + b) * (a - b)
print("The result of the expression is: " + str(result))

# In Python, you can also use the `math` module to perform more advanced mathematical operations. For example:
import math
sqrt_a = math.sqrt(a)
print("The square root of a is: " + str(sqrt_a))
log_a = math.log(a)
print("The natural logarithm of a is: " + str(log_a))
sin_a = math.sin(a)
print("The sine of a is: " + str(sin_a))

# In Python, you can also use the `random` module to generate random numbers. For example:
import random
random_number = random.randint(1, 100)
print("A random number between 1 and 100 is: " + str(random_number))

# Intendation in Python is crucial as it defines the scope of loops, functions, and other code blocks. Proper indentation is necessary to avoid syntax errors and to ensure that the code executes correctly. In Python, it is common to use four spaces for indentation. For example:
if a > b:
    print("a is greater than b")
else:
    print("b is greater than or equal to a")

# In Python, you can also use the `with` statement to manage resources such as file handling. The `with` statement ensures that resources are properly cleaned up after use. For example:
with open('example.txt', 'w') as file:
    file.write("This is an example of using the with statement for file handling.")

# In Python, you can also use the `try` and `except` statements to handle exceptions and errors in your code. This allows you to gracefully handle errors without crashing your program. For example:
try:
    result = a / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

#Variables Naming Rules 
# ✅ Valid names
my_name = "Alice"
age1 = 25
_private = "hidden"
firstName = "John"      # camelCase (not recommended in Python)
first_name = "John"     # snake_case ✅ Python standard

""" # ❌ Invalid names
2name = "Alice"         # cannot start with number
my-name = "Alice"       # no hyphens allowed
my name = "Alice"       # no spaces allowed
class = "Python"        # cannot use reserved keywords
"""

# Reserved Keywords in Python 
# and , as , assert , break , class , continue , def , del , elif , else , except , finally , for , from , global , if , import , in , is , lambda , nonlocal , not , or , pass , raise , return , try , while , with , yield

import keyword
print((keyword.kwlist))  # prints all reserved words in Python

# String in Depth 
# Multiline Strings 
multiline_string = """This is a multiline string.
It can span multiple lines.
You can use triple quotes to create it."""
print(multiline_string)

# String indexing and slicing 
my_string = "Hello, World!"
# Indexing
first_character = my_string[0]  # 'H'
last_character = my_string[-1]  # '!'
print("First character:", first_character)
print("Last character:", last_character)
# Slicing
substring = my_string[0:5]  # 'Hello'
print("Substring:", substring)

# Useful string methods 
my_string = "Hello, World!"
# Convert to uppercase
uppercase_string = my_string.upper()
print("Uppercase:", uppercase_string)
# Convert to lowercase
lowercase_string = my_string.lower()
print("Lowercase:", lowercase_string)
# Replace a substring
replaced_string = my_string.replace("World", "Python")
print("Replaced String:", replaced_string)
# Split a string into a list
split_string = my_string.split(", ")
print("Split String:", split_string)
# Join a list into a string
joined_string = " ".join(split_string)
print("Joined String:", joined_string)

# String Formatting 
name = "Alice"
age = 25
# Using f-strings (Python 3.6+)
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
# Using str.format() method
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)
# Using % operator
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)

# Getting User Input 
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")
user_age = input("Enter your age: ")
print("You are " + user_age + " years old.")

# Python convention 
# 1. Use snake_case for variable and function names (e.g., my_variable, calculate_sum).
# 2. Use PascalCase for class names (e.g., MyClass, UserProfile
# 3. Use all uppercase letters with underscores for constants (e.g., MAX_VALUE, PI).
# 4. Avoid using single-letter variable names except for loop counters (e.g., i, j, k).
# 5. Be consistent with your naming conventions throughout your code.