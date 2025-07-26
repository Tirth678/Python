# we often decleare a vairable to store user input
# we can take normal input as
x = input("Enter any random value")
print(x)
# every input by default in python is considered as string

# to change this we can add datatype before input
user_input_numerical = int(input("Enter a value"))
print(user_input_numerical)
# here now user has to enter value which is an integer

user_input_float = float(input("Enter a value"))
print(user_input_float)
# here now user has to enter value in floating integer

user_input_default = str(input("Enter a value"))
print(user_input_default)
# user has to enter a value which is string

user_input_weird = bool(input("Enter a value"))
print(user_input_weird)
# user has to enter a value which is either True or False

user_input_list = list(input("Enter a value"))
print(user_input_list)
# whatever user enters will be stored in list as elements with indexing

user_input_tuple = tuple(input("Enter a value"))
print(user_input_tuple) 
# now input will be stored as elements of tuple

# Python Input and Output Statements - Complete Usage Guide

print("=" * 70)
print("PYTHON INPUT AND OUTPUT STATEMENTS USAGE")
print("=" * 70)

# 1. BASIC OUTPUT STATEMENTS
print("\n1. BASIC OUTPUT STATEMENTS")
print("-" * 40)

# Simple print statements
print("Hello, World!")
print("Python Programming")
print("Learning Input/Output")

# Multiple arguments in print
print("Name:", "Alice", "Age:", 25)
print("Values:", 10, 20, 30, 40, 50)

# Print with different data types
name = "Bob"
age = 30
height = 5.9
is_student = True
print("Mixed types:", name, age, height, is_student)

# 2. PRINT FUNCTION PARAMETERS
print("\n\n2. PRINT FUNCTION PARAMETERS")
print("-" * 40)

# sep parameter - separator between values
print("Apple", "Banana", "Cherry", sep=", ")
print("2024", "12", "25", sep="-")
print("Value1", "Value2", "Value3", sep=" | ")

# end parameter - what to print at the end
print("Hello", end=" ")
print("World!")  # Same line

print("Loading", end="")
for i in range(5):
    print(".", end="", flush=True)
print(" Done!")

# flush parameter - force output immediately
import time
print("\nProgress: ", end="", flush=True)
for i in range(5):
    print(f"{i+1}", end=" ", flush=True)
    time.sleep(0.5)
print("Complete!")

# 3. FORMATTED OUTPUT METHODS
print("\n\n3. FORMATTED OUTPUT METHODS")
print("-" * 40)

# Method 1: % formatting (old style)
name = "Charlie"
score = 95.5
print("Student: %s, Score: %.1f%%" % (name, score))
print("Integer: %d, Float: %.2f, String: %s" % (42, 3.14159, "Hello"))

# Method 2: .format() method
print("Student: {}, Score: {:.1f}%".format(name, score))
print("Values: {0}, {1}, {0}".format("A", "B"))  # Positional
print("Person: {name}, Age: {age}".format(name="David", age=28))  # Named

# Method 3: f-strings (Python 3.6+) - Recommended
age = 25
salary = 50000
print(f"Employee: {name}, Age: {age}, Salary: ${salary:,}")
print(f"Calculation: {10} + {20} = {10 + 20}")
print(f"Percentage: {score:.2f}%")

# 4. ADVANCED FORMATTING
print("\n\n4. ADVANCED FORMATTING")
print("-" * 40)

# Number formatting
number = 1234567.89
print(f"Default: {number}")
print(f"Comma separator: {number:,}")
print(f"Two decimal places: {number:.2f}")
print(f"Scientific notation: {number:.2e}")
print(f"Percentage: {0.1234:.1%}")

# String formatting
text = "python"
print(f"Original: '{text}'")
print(f"Uppercase: '{text.upper()}'")
print(f"Centered (20): '{text:^20}'")
print(f"Left aligned (15): '{text:<15}'")
print(f"Right aligned (15): '{text:>15}'")

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"Current date: {now:%Y-%m-%d}")
print(f"Current time: {now:%H:%M:%S}")
print(f"Full datetime: {now:%Y-%m-%d %H:%M:%S}")

# 5. BASIC INPUT STATEMENTS
print("\n\n5. BASIC INPUT STATEMENTS")
print("-" * 40)

# Note: In a real interactive environment, these would pause for user input
# For demonstration, we'll show the syntax and simulate inputs

print("# Basic input syntax:")
print("name = input('Enter your name: ')")
print("# User would type: Alice")
name = "Alice"  # Simulated input
print(f"Hello, {name}!")

print("\n# Input always returns string:")
print("age_str = input('Enter your age: ')")
print("# User would type: 25")
age_str = "25"  # Simulated input
print(f"Type of input: {type(age_str)}")
print(f"Value: '{age_str}'")

# 6. INPUT TYPE CONVERSION
print("\n\n6. INPUT TYPE CONVERSION")
print("-" * 40)

# Converting string input to numbers
print("# Converting to integer:")
print("age = int(input('Enter age: '))")
age = int("25")  # Simulated
print(f"Age: {age} (type: {type(age).__name__})")

print("\n# Converting to float:")
print("height = float(input('Enter height: '))")
height = float("5.9")  # Simulated
print(f"Height: {height} (type: {type(height).__name__})")

print("\n# Converting to boolean:")
print("is_student = input('Are you a student? (yes/no): ').lower() == 'yes'")
is_student = "yes".lower() == "yes"  # Simulated
print(f"Student status: {is_student} (type: {type(is_student).__name__})")

# 7. INPUT VALIDATION AND ERROR HANDLING
print("\n\n7. INPUT VALIDATION AND ERROR HANDLING")
print("-" * 40)

def get_integer_input(prompt, min_val=None, max_val=None):
    """Simulate getting valid integer input with validation"""
    print(f"Function: get_integer_input('{prompt}')")
    
    # Simulate different scenarios
    test_inputs = ["25", "abc", "-5", "100"]
    
    for test_input in test_inputs:
        print(f"Simulating input: '{test_input}'")
        try:
            value = int(test_input)
            if min_val is not None and value < min_val:
                print(f"  Error: Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"  Error: Value must be at most {max_val}")
                continue
            print(f"  Valid input: {value}")
            return value
        except ValueError:
            print(f"  Error: '{test_input}' is not a valid integer")
    
    return 25  # Default for simulation

# Test validation function
print("Testing input validation:")
age = get_integer_input("Enter your age (18-100): ", min_val=18, max_val=100)
print(f"Final age: {age}")

# 8. MULTIPLE INPUTS
print("\n\n8. MULTIPLE INPUTS")
print("-" * 40)

# Single line multiple inputs
print("# Getting multiple values in one line:")
print("x, y, z = input('Enter three numbers: ').split()")
print("# User would type: 10 20 30")
x, y, z = "10 20 30".split()  # Simulated
print(f"Values: x='{x}', y='{y}', z='{z}'")

# Converting multiple inputs
print("\n# Converting multiple inputs:")
numbers = list(map(int, "10 20 30".split()))
print(f"Converted numbers: {numbers}")

# Getting multiple inputs separately
print("\n# Multiple separate inputs:")
print("name = input('Name: ')")
print("age = int(input('Age: '))")
print("city = input('City: ')")
# Simulated values
personal_info = {
    'name': 'Bob',
    'age': 30,
    'city': 'New York'
}
print(f"Personal info: {personal_info}")

# 9. PRACTICAL INPUT/OUTPUT EXAMPLES
print("\n\n9. PRACTICAL INPUT/OUTPUT EXAMPLES")
print("-" * 40)

# Example 1: Calculator
print("=== CALCULATOR EXAMPLE ===")
def calculator_demo():
    print("Simple Calculator")
    # Simulated inputs
    num1 = 15
    num2 = 4
    operation = "+"
    
    print(f"First number: {num1}")
    print(f"Second number: {num2}")
    print(f"Operation: {operation}")
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operation"
    
    print(f"Result: {num1} {operation} {num2} = {result}")

calculator_demo()

# Example 2: Student Grade System
print("\n=== STUDENT GRADE SYSTEM ===")
def grade_system_demo():
    print("Student Grade Calculator")
    # Simulated inputs
    student_name = "Emma Wilson"
    subjects = ["Math", "Science", "English"]
    scores = [85, 92, 78]
    
    print(f"Student Name: {student_name}")
    print("Subject Scores:")
    
    total = 0
    for subject, score in zip(subjects, scores):
        print(f"  {subject}: {score}")
        total += score
    
    average = total / len(scores)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"\nResults:")
    print(f"Total Score: {total}")
    print(f"Average: {average:.1f}")
    print(f"Grade: {grade}")

grade_system_demo()

# Example 3: Personal Information Form
print("\n=== PERSONAL INFORMATION FORM ===")
def personal_form_demo():
    print("Personal Information Form")
    # Simulated inputs
    form_data = {
        'full_name': 'John Smith',
        'age': 28,
        'email': 'john.smith@email.com',
        'phone': '+1-555-123-4567',
        'address': '123 Main St, City, State',
        'occupation': 'Software Engineer'
    }
    
    print("\nCollected Information:")
    print("-" * 25)
    for key, value in form_data.items():
        formatted_key = key.replace('_', ' ').title()
        print(f"{formatted_key:12}: {value}")

personal_form_demo()

# 10. FILE INPUT/OUTPUT BASICS
print("\n\n10. FILE INPUT/OUTPUT BASICS")
print("-" * 40)

# Writing to file
print("=== WRITING TO FILE ===")
filename = "sample_output.txt"
data_to_write = [
    "Hello, World!",
    "This is a sample file.",
    "Created using Python I/O operations.",
    f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
]

# Simulate file writing
print(f"Writing to file: {filename}")
for line in data_to_write:
    print(f"  Writing: {line}")

# Reading from file (simulated)
print(f"\n=== READING FROM FILE ===")
print(f"Reading from file: {filename}")
print("File contents:")
for i, line in enumerate(data_to_write, 1):
    print(f"  Line {i}: {line}")

# 11. FORMATTED TABLES AND REPORTS
print("\n\n11. FORMATTED TABLES AND REPORTS")
print("-" * 40)

# Employee report example
employees = [
    {"name": "Alice Johnson", "id": 1001, "salary": 75000, "department": "Engineering"},
    {"name": "Bob Smith", "id": 1002, "salary": 68000, "department": "Marketing"},
    {"name": "Carol Davis", "id": 1003, "salary": 82000, "department": "Sales"},
    {"name": "David Wilson", "id": 1004, "salary": 71000, "department": "Engineering"}
]

print("EMPLOYEE REPORT")
print("=" * 60)
print(f"{'ID':<6} {'Name':<15} {'Department':<12} {'Salary':<10}")
print("-" * 60)

for emp in employees:
    print(f"{emp['id']:<6} {emp['name']:<15} {emp['department']:<12} ${emp['salary']:<9,}")

print("-" * 60)
total_salary = sum(emp['salary'] for emp in employees)
avg_salary = total_salary / len(employees)
print(f"{'Total':<33} ${total_salary:,}")
print(f"{'Average':<33} ${avg_salary:,.0f}")

# 12. INTERACTIVE MENU SYSTEM
print("\n\n12. INTERACTIVE MENU SYSTEM")
print("-" * 40)

def menu_system_demo():
    """Demonstrate a menu-driven program structure"""
    print("=== RESTAURANT MENU SYSTEM ===")
    
    menu_items = {
        1: {"name": "Burger", "price": 12.99},
        2: {"name": "Pizza", "price": 15.99},
        3: {"name": "Salad", "price": 8.99},
        4: {"name": "Pasta", "price": 13.99},
        5: {"name": "Drink", "price": 2.99}
    }
    
    print("\nMENU:")
    print("-" * 30)
    for item_id, item in menu_items.items():
        print(f"{item_id}. {item['name']:<10} ${item['price']:.2f}")
    
    # Simulate user selections
    order = [1, 2, 5]  # Burger, Pizza, Drink
    print(f"\nSimulated order: {order}")
    
    print("\nORDER SUMMARY:")
    print("-" * 30)
    total = 0
    
    for item_id in order:
        if item_id in menu_items:
            item = menu_items[item_id]
            print(f"{item['name']:<10} ${item['price']:.2f}")
            total += item['price']
    
    tax = total * 0.08  # 8% tax
    final_total = total + tax
    
    print("-" * 30)
    print(f"Subtotal:   ${total:.2f}")
    print(f"Tax (8%):   ${tax:.2f}")
    print(f"Total:      ${final_total:.2f}")

menu_system_demo()

# 13. DATA COLLECTION AND PROCESSING
print("\n\n13. DATA COLLECTION AND PROCESSING")
print("-" * 40)

def survey_demo():
    """Demonstrate data collection and analysis"""
    print("=== CUSTOMER SATISFACTION SURVEY ===")
    
    # Simulated survey responses
    responses = [
        {"name": "Alice", "rating": 5, "comment": "Excellent service!"},
        {"name": "Bob", "rating": 4, "comment": "Very good, minor issues."},
        {"name": "Carol", "rating": 5, "comment": "Outstanding experience!"},
        {"name": "David", "rating": 3, "comment": "Average, could be better."},
        {"name": "Eve", "rating": 4, "comment": "Good overall satisfaction."}
    ]
    
    print(f"Collected {len(responses)} responses:")
    print("-" * 40)
    
    total_rating = 0
    for i, response in enumerate(responses, 1):
        print(f"{i}. {response['name']}: {response['rating']}/5")
        print(f"   Comment: {response['comment']}")
        total_rating += response['rating']
    
    average_rating = total_rating / len(responses)
    
    print("-" * 40)
    print(f"Average Rating: {average_rating:.1f}/5")
    
    # Rating distribution
    rating_counts = {}
    for response in responses:
        rating = response['rating']
        rating_counts[rating] = rating_counts.get(rating, 0) + 1
    
    print("\nRating Distribution:")
    for rating in sorted(rating_counts.keys(), reverse=True):
        count = rating_counts[rating]
        percentage = (count / len(responses)) * 100
        stars = "★" * rating + "☆" * (5 - rating)
        print(f"{stars} ({rating}): {count} responses ({percentage:.1f}%)")

survey_demo()

# 14. BEST PRACTICES SUMMARY
print("\n\n14. INPUT/OUTPUT BEST PRACTICES")
print("-" * 40)

print("""
OUTPUT BEST PRACTICES:
1. Use f-strings for formatting (Python 3.6+)
2. Use appropriate formatting for numbers and dates
3. Provide clear, descriptive output messages
4. Use consistent formatting throughout your program
5. Consider using tables for structured data
6. Include units and context in output

INPUT BEST PRACTICES:
1. Always validate user input
2. Provide clear prompts and instructions
3. Handle invalid input gracefully
4. Use appropriate data type conversions
5. Give feedback on input errors
6. Consider default values for optional inputs

EXAMPLE VALIDATION FUNCTION:
def get_validated_input(prompt, data_type=str, validator=None):
    while True:
        try:
            user_input = input(prompt)
            converted_value = data_type(user_input)
            if validator and not validator(converted_value):
                print("Invalid input. Please try again.")
                continue
            return converted_value
        except ValueError:
            print(f"Please enter a valid {data_type.__name__}.")

USAGE EXAMPLES:
- age = get_validated_input("Enter age: ", int, lambda x: 0 <= x <= 120)
- email = get_validated_input("Enter email: ", str, lambda x: "@" in x)
""")

print("\n" + "=" * 70)
print("INPUT/OUTPUT STATEMENTS DEMONSTRATION COMPLETE")
print("=" * 70)

# Summary of covered topics
print("\nTOPICS COVERED:")
print("✓ Basic print statements and parameters")
print("✓ Formatted output (%, .format(), f-strings)")
print("✓ Advanced formatting options")
print("✓ Input statements and type conversion")
print("✓ Input validation and error handling")
print("✓ Multiple inputs and data processing")
print("✓ Practical examples and applications")
print("✓ File I/O basics")
print("✓ Formatted reports and tables")
print("✓ Interactive menu systems")
print("✓ Data collection and analysis")
print("✓ Best practices and recommendations")