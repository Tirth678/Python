

# Integer
age = 25
student_count = 150
negative_num = -42
print(f"Integer examples:")
print(f"age = {age} (type: {type(age).__name__})")
print(f"student_count = {student_count}")
print(f"negative_num = {negative_num}")

# Float
height = 5.9
temperature = 98.6
pi = 3.14159
scientific_notation = 1.5e3  # 1500.0
print(f"\nFloat examples:")
print(f"height = {height} (type: {type(height).__name__})")
print(f"temperature = {temperature}")
print(f"pi = {pi}")
print(f"scientific_notation = {scientific_notation}")

# String
name = "Alice Johnson"
message = 'Hello, World!'
multiline = """This is a
multiline string"""
empty_string = ""
print(f"\nString examples:")
print(f"name = '{name}' (type: {type(name).__name__})")
print(f"message = '{message}'")
print(f"multiline = '{multiline}'")
print(f"empty_string = '{empty_string}' (length: {len(empty_string)})")

# Boolean
is_student = True
is_graduated = False
has_license = True
print(f"\nBoolean examples:")
print(f"is_student = {is_student} (type: {type(is_student).__name__})")
print(f"is_graduated = {is_graduated}")
print(f"has_license = {has_license}")

# 2. COMPLEX DATA TYPES
print("\n\n2. COMPLEX DATA TYPES")
print("-" * 30)

# Lists
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
empty_list = []
print(f"List examples:")
print(f"fruits = {fruits} (type: {type(fruits).__name__})")
print(f"numbers = {numbers}")
print(f"mixed_list = {mixed_list}")
print(f"empty_list = {empty_list}")

# Tuples
coordinates = (10, 20)
rgb_color = (255, 128, 0)
single_item_tuple = (42,)  # Note the comma
mixed_tuple = ("John", 25, True)
print(f"\nTuple examples:")
print(f"coordinates = {coordinates} (type: {type(coordinates).__name__})")
print(f"rgb_color = {rgb_color}")
print(f"single_item_tuple = {single_item_tuple}")
print(f"mixed_tuple = {mixed_tuple}")

# Dictionaries
student_info = {
    "name": "Bob Smith",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics", "Chemistry"]
}
empty_dict = {}
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(f"\nDictionary examples:")
print(f"student_info = {student_info}")
print(f"empty_dict = {empty_dict} (type: {type(empty_dict).__name__})")
print(f"nested_dict = {nested_dict}")

# Sets
unique_numbers = {1, 2, 3, 4, 5}
colors = {"red", "green", "blue", "red"}  # Duplicates removed
empty_set = set()  # {} creates empty dict, not set
print(f"\nSet examples:")
print(f"unique_numbers = {unique_numbers} (type: {type(unique_numbers).__name__})")
print(f"colors = {colors}")  # Note: duplicates removed
print(f"empty_set = {empty_set}")

# 3. ARITHMETIC OPERATORS
print("\n\n3. ARITHMETIC OPERATORS")
print("-" * 30)

a = 15
b = 4
print(f"Given: a = {a}, b = {b}")
print(f"Addition: a + b = {a + b}")
print(f"Subtraction: a - b = {a - b}")
print(f"Multiplication: a * b = {a * b}")
print(f"Division: a / b = {a / b}")
print(f"Floor Division: a // b = {a // b}")
print(f"Modulus: a % b = {a % b}")
print(f"Exponentiation: a ** b = {a ** b}")

# Operator precedence example
expression_result = 2 + 3 * 4 ** 2 - 1
print(f"\nOperator Precedence:")
print(f"2 + 3 * 4 ** 2 - 1 = {expression_result}")
print("Order: 4**2=16, 3*16=48, 2+48=50, 50-1=49")

# 4. COMPARISON OPERATORS
print("\n\n4. COMPARISON OPERATORS")
print("-" * 30)

x = 10
y = 20
z = 10
print(f"Given: x = {x}, y = {y}, z = {z}")
print(f"Equal: x == z = {x == z}")
print(f"Not Equal: x != y = {x != y}")
print(f"Greater than: y > x = {y > x}")
print(f"Less than: x < y = {x < y}")
print(f"Greater or equal: x >= z = {x >= z}")
print(f"Less or equal: x <= y = {x <= y}")

# String comparisons
str1 = "apple"
str2 = "banana"
str3 = "apple"
print(f"\nString comparisons:")
print(f"'{str1}' == '{str3}' = {str1 == str3}")
print(f"'{str1}' < '{str2}' = {str1 < str2}")  # Lexicographic order

# 5. LOGICAL OPERATORS
print("\n\n5. LOGICAL OPERATORS")
print("-" * 30)

p = True
q = False
r = True
print(f"Given: p = {p}, q = {q}, r = {r}")
print(f"AND: p and r = {p and r}")
print(f"OR: p or q = {p or q}")
print(f"NOT: not q = {not q}")
print(f"Complex: (p and r) or (not q) = {(p and r) or (not q)}")

# Logical with numbers (truthy/falsy values)
num1 = 0    # Falsy
num2 = 5    # Truthy
print(f"\nTruthy/Falsy values:")
print(f"bool(0) = {bool(num1)}")
print(f"bool(5) = {bool(num2)}")
print(f"5 and 0 = {num2 and num1}")
print(f"5 or 0 = {num2 or num1}")

# 6. ASSIGNMENT OPERATORS
print("\n\n6. ASSIGNMENT OPERATORS")
print("-" * 30)

counter = 10
print(f"Initial counter = {counter}")

counter += 5   # counter = counter + 5
print(f"After += 5: counter = {counter}")

counter -= 3   # counter = counter - 3
print(f"After -= 3: counter = {counter}")

counter *= 2   # counter = counter * 2
print(f"After *= 2: counter = {counter}")

counter //= 4  # counter = counter // 4
print(f"After //= 4: counter = {counter}")

counter **= 2  # counter = counter ** 2
print(f"After **= 2: counter = {counter}")

# 7. MEMBERSHIP AND IDENTITY OPERATORS
print("\n\n7. MEMBERSHIP AND IDENTITY OPERATORS")
print("-" * 30)

# Membership operators
fruits_list = ["apple", "banana", "orange"]
print(f"fruits_list = {fruits_list}")
print(f"'apple' in fruits_list = {'apple' in fruits_list}")
print(f"'grape' not in fruits_list = {'grape' not in fruits_list}")

text = "Hello World"
print(f"\ntext = '{text}'")
print(f"'World' in text = {'World' in text}")
print(f"'xyz' not in text = {'xyz' not in text}")

# Identity operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"\nIdentity operators:")
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")
print(f"list1 is list3 = {list1 is list3}")  # Same object
print(f"list1 is list2 = {list1 is list2}")  # Different objects
print(f"list1 == list2 = {list1 == list2}")  # Same content

# 8. STRING OPERATORS AND METHODS
print("\n\n8. STRING OPERATORS AND METHODS")
print("-" * 30)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
repeated = "Hi! " * 3  # Repetition

print(f"String operations:")
print(f"first_name = '{first_name}'")
print(f"last_name = '{last_name}'")
print(f"Concatenation: '{full_name}'")
print(f"Repetition: '{repeated}'")

# String methods
sample_text = "  Python Programming  "
print(f"\nString methods:")
print(f"Original: '{sample_text}'")
print(f"Upper: '{sample_text.upper()}'")
print(f"Lower: '{sample_text.lower()}'")
print(f"Strip: '{sample_text.strip()}'")
print(f"Length: {len(sample_text)}")
print(f"Replace: '{sample_text.replace('Python', 'Java')}'")

# 9. COMPLEX EXPRESSIONS
print("\n\n9. COMPLEX EXPRESSIONS")
print("-" * 30)

# Mathematical expressions
radius = 5
area = 3.14159 * radius ** 2
circumference = 2 * 3.14159 * radius
print(f"Circle calculations (radius = {radius}):")
print(f"Area = π × r² = {area:.2f}")
print(f"Circumference = 2 × π × r = {circumference:.2f}")

# Conditional expressions (ternary operator)
score = 85
grade = "Pass" if score >= 60 else "Fail"
print(f"\nConditional expression:")
print(f"Score: {score}, Grade: {grade}")

# Complex boolean expressions
age = 22
has_id = True
is_weekend = False
can_enter = (age >= 18 and has_id) or (age >= 21 and not is_weekend)
print(f"\nComplex boolean:")
print(f"Age: {age}, Has ID: {has_id}, Weekend: {is_weekend}")
print(f"Can enter: {can_enter}")

# 10. TYPE CONVERSION AND CHECKING
print("\n\n10. TYPE CONVERSION AND CHECKING")
print("-" * 30)

# Type conversion
str_num = "123"
int_num = int(str_num)
float_num = float(str_num)
bool_num = bool(int_num)

print(f"Type conversions:")
print(f"str_num = '{str_num}' ({type(str_num).__name__})")
print(f"int(str_num) = {int_num} ({type(int_num).__name__})")
print(f"float(str_num) = {float_num} ({type(float_num).__name__})")
print(f"bool(int_num) = {bool_num} ({type(bool_num).__name__})")

# Type checking
values = [42, "hello", 3.14, True, [1, 2, 3]]
print(f"\nType checking:")
for value in values:
    print(f"{value} is {type(value).__name__}")

# isinstance() function
print(f"\nUsing isinstance():")
print(f"isinstance(42, int) = {isinstance(42, int)}")
print(f"isinstance('hello', str) = {isinstance('hello', str)}")
print(f"isinstance([1, 2, 3], list) = {isinstance([1, 2, 3], list)}")

# 11. PRACTICAL EXAMPLES
print("\n\n11. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Grade calculator
math_score = 85
science_score = 92
english_score = 78
total_score = math_score + science_score + english_score
average_score = total_score / 3
is_honor_roll = average_score >= 85 and all([math_score >= 80, science_score >= 80, english_score >= 80])

print(f"Grade Calculator:")
print(f"Math: {math_score}, Science: {science_score}, English: {english_score}")
print(f"Total: {total_score}, Average: {average_score:.1f}")
print(f"Honor Roll: {is_honor_roll}")

# Example 2: Shopping cart
item_prices = [19.99, 5.50, 12.75, 8.25]
tax_rate = 0.08
subtotal = sum(item_prices)
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount
discount = 5.00 if subtotal > 40 else 0
final_total = total - discount

print(f"\nShopping Cart:")
print(f"Items: {item_prices}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax_amount:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")

# Example 3: Text analysis
text_sample = "Python is a powerful programming language. Python is easy to learn!"
word_count = len(text_sample.split())
char_count = len(text_sample)
python_mentions = text_sample.lower().count("python")
has_exclamation = "!" in text_sample

print(f"\nText Analysis:")
print(f"Text: '{text_sample}'")
print(f"Word count: {word_count}")
print(f"Character count: {char_count}")
print(f"'Python' mentions: {python_mentions}")
print(f"Has exclamation: {has_exclamation}")

print("\n" + "=" * 60)
print("END OF DEMO")
print("=" * 60)