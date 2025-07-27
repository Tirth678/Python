# working of decision statements
age = 18
if age >= 18:
    print("You are eligible to vote")

# if-else statements
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")

# if-elif-else statements
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

# nested if-else statements
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")
else:
    print("You're too young to drive")

# logical operatoes
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Access granted")
elif username == "admin" or password == "secret123":
    print("Partial credentials correct")
else:
    print("Access denied")

# Using not operator
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Access granted")
elif username == "admin" or password == "secret123":
    print("Partial credentials correct")
else:
    print("Access denied")

# Using not operator
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Access granted")
elif username == "admin" or password == "secret123":
    print("Partial credentials correct")
else:
    print("Access denied")

# Using not operator
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Access granted")
elif username == "admin" or password == "secret123":
    print("Partial credentials correct")
else:
    print("Access denied")

# Using not operator
is_weekend = False
if not is_weekend:
    print("It's a weekday")

fruits = ["apple", "banana", "orange"]
fruit = "apple"

if fruit in fruits:
    print(f"{fruit} is available")

x = None
if x is None:
    print("x is None")

# one-line or short cirucuit evaluation
x = 0
# This won't cause division by zero error because x == 0 is checked first
if x != 0 and 10/x > 2:
    print("This won't execute")

# ternary operator
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # Output: adult