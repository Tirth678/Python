# What are Variables and Identifiers?
# Variables are containers that store data in memory. 
# Think of them as labeled boxes where you can put different types of information (dabba).
# Identifiers are the names we give to variables, functions, classes, and other programming elements. 
# They're like labels on those boxes.

a = 12 # this is variable named as "a" which stores value of integer 12 
b = 12.0 # this is variable named as "b" which stores value of floating point integer 12
c = True # this is variable named as "c" which stores value of boolean expression True in c
d = "Hi" # string
e = [1,2,3] # list
f = (1,2,3) # tuples
g = {"a": "1"} # dictionary

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# now as this are variables, values can be changed and new values can be assigned.
a = 10 # now a's new value is 10 instead of 12
print(f"New value of a = {a}")

# examples
# 1. BASIC VARIABLE DECLARATION AND ASSIGNMENT
print("=== Basic Variables ===")
name = "Alice"              # String variable
age = 25                    # Integer variable
height = 5.6               # Float variable
is_student = True          # Boolean variable

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# 2. VALID AND INVALID IDENTIFIERS
print("\n=== Valid Identifiers ===")
student_name = "Bob"       # Valid: uses underscore
firstName = "Charlie"      # Valid: camelCase
_private_var = 42         # Valid: starts with underscore
name2 = "David"           # Valid: contains number

print(f"student_name: {student_name}")
print(f"firstName: {firstName}")
print(f"_private_var: {_private_var}")
print(f"name2: {name2}")

# Invalid identifiers (commented out to avoid errors):
# 2name = "Error"          # Invalid: starts with number
# class = "Error"          # Invalid: reserved keyword
# my-var = "Error"         # Invalid: contains hyphen

# 3. VARIABLE REASSIGNMENT
print("\n=== Variable Reassignment ===")
counter = 10
print(f"Initial counter: {counter}")

counter = counter + 5      # Reassign with new value
print(f"After addition: {counter}")

counter = "Now I'm a string!"  # Variables can change type
print(f"Changed to string: {counter}")

# 4. MULTIPLE ASSIGNMENT
print("\n=== Multiple Assignment ===")
x, y, z = 1, 2, 3         # Assign multiple variables at once
print(f"x: {x}, y: {y}, z: {z}")

a = b = c = 100           # Assign same value to multiple variables
print(f"a: {a}, b: {b}, c: {c}")

# 5. SIMPLE CALCULATOR PROGRAM
print("\n=== Simple Calculator ===")
num1 = 15
num2 = 4

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")

# 6. STUDENT GRADE PROGRAM
print("\n=== Student Grade Calculator ===")
student_name = "Emma"
math_score = 85
science_score = 92
english_score = 78

total_marks = math_score + science_score + english_score
average = total_marks / 3

print(f"Student: {student_name}")
print(f"Math: {math_score}")
print(f"Science: {science_score}")
print(f"English: {english_score}")
print(f"Total: {total_marks}")
print(f"Average: {average:.2f}")

# Determine grade based on average
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Grade: {grade}")

# 7. TEMPERATURE CONVERTER
print("\n=== Temperature Converter ===")
celsius = 25
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Temperature Conversions:")
print(f"{celsius}°C = {fahrenheit}°F")
print(f"{celsius}°C = {kelvin}K")

# 8. VARIABLE SCOPE DEMONSTRATION
print("\n=== Variable Scope ===")
global_var = "I'm global"

def demonstrate_scope():
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

demonstrate_scope()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause an error - local_var not accessible

# 9. NAMING CONVENTIONS EXAMPLES
print("\n=== Naming Conventions ===")
# Good naming practices
user_age = 30              # Descriptive, snake_case
MAX_ATTEMPTS = 3           # Constants in UPPER_CASE
is_valid = True            # Boolean with is_ prefix
total_count = 0            # Clear purpose

# Poor naming practices (functional but not recommended)
x = 30                     # Not descriptive
data = True               # Vague name
temp = 0                  # Abbreviation not clear

print("Good naming makes code self-documenting!")
print(f"User age: {user_age}, Max attempts: {MAX_ATTEMPTS}")

# 10. COMMON VARIABLE OPERATIONS
print("\n=== Common Operations ===")
# String operations
greeting = "Hello"
name = "World"
message = greeting + " " + name + "!"
print(f"Concatenation: {message}")

# Numeric operations
base_price = 100
tax_rate = 0.08
tax_amount = base_price * tax_rate
total_price = base_price + tax_amount
print(f"Price calculation: ${base_price} + ${tax_amount:.2f} = ${total_price:.2f}")

# List operations
numbers = [1, 2, 3, 4, 5]
first_number = numbers[0]
last_number = numbers[-1]
list_length = len(numbers)
print(f"List: {numbers}")
print(f"First: {first_number}, Last: {last_number}, Length: {list_length}")
