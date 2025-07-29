# usage of break, continue and pass statements
# pass is used to often leave space for another user to complete your code, or just leaving that space for future reference

def factorial(x):
    if x == 0 or x == 1:  # Fixed condition
        return 1
    else:
        pass  # Placeholder for future implementation

# Basic Usage Examples:

# Skipping specific values:
# python
# Print only odd numbers
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue  # skip even numbers
#     print(i)
# Output: 1, 3, 5, 7, 9

# Processing valid input only:
# python
# names = ["Alice", "", "Bob", "   ", "Charlie", None]
# for name in names:
#     if not name or not name.strip():
#         continue  # skip empty or whitespace-only names
#     print(f"Hello, {name.strip()}!")
# Output: Hello, Alice!
#         Hello, Bob!
#         Hello, Charlie!

# File processing with error handling:
# python
# files = ["file1.txt", "file2.txt", "corrupted.txt", "file3.txt"]
# for filename in files:
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             if len(content) == 0:
#                 continue  # skip empty files
#             print(f"Processing {filename}: {len(content)} characters")
#     except FileNotFoundError:
#         print(f"File {filename} not found, skipping...")
#         continue  # skip to next file

# break Statement
# The break statement immediately exits the current loop entirely.

# Basic Usage Examples:
# Early termination based on condition:
# python
# numbers = [1, 5, 3, -2, 8, 4]
# for i, num in enumerate(numbers):
#     if num < 0:
#         print(f"First negative number {num} found at index {i}")
#         break
#     print(f"Checking positive number: {num}")
# Output: Checking positive number: 1
#         Checking positive number: 5
#         Checking positive number: 3
#         First negative number -2 found at index 1

# User input validation with exit option:
# python
# while True:
#     password = input("Enter password (or 'exit' to quit): ")
#     if password.lower() == 'exit':
#         print("Goodbye!")
#         break
#     if len(password) >= 8:
#         print("Password accepted!")
#         break
#     else:
#         print("Password too short. Must be at least 8 characters.")

# Search and stop:
# python
# students = [
#     {"name": "Alice", "grade": 85},
#     {"name": "Bob", "grade": 92},
#     {"name": "Charlie", "grade": 78}
# ]
# search_name = "Bob"
# for student in students:
#     if student["name"] == search_name:
#         print(f"Found {search_name} with grade {student['grade']}")
#         break
# else:
#     print(f"{search_name} not found")  # executes only if break wasn't called

# pass Statement
# The pass statement is a null operation - it does nothing when executed. It's used as a placeholder.

# Basic Usage Examples:
# Function stubs during development:
# python
# def calculate_tax(income):
#     pass  # TODO: implement tax calculation
# def send_email(recipient, message):
#     pass  # TODO: implement email sending
# def validate_user(username, password):
#     pass  # TODO: implement user validation

# Empty exception handling:
# python
# def safe_divide(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         pass  # silently ignore division by zero
#     except TypeError:
#         print("Invalid input types")
#     return None
# print(safe_divide(10, 0))  # Returns None, no error message
# print(safe_divide(10, 2))  # Returns 5.0

# Conditional blocks that need no action:
# def process_user_role(role):
#     if role == "admin":
#         print("Granting admin privileges")
#     elif role == "user":
#         print("Granting user privileges")
#     elif role == "guest":
#         pass  # guests get no special privileges
#     else:
#         print("Unknown role")
# process_user_role("guest")  # No output

# Combining All Three Statements
# Real-world Example: Data Processing Pipeline
# python
# def process_data_batch(data_list):
#     processed_count = 0
#     error_count = 0
#     for i, data_item in enumerate(data_list):
#         print(f"Processing item {i+1}/{len(data_list)}")
#         if data_item is None or data_item == "":
#             print("  Skipping empty item")
#             continue
#         if data_item == "STOP":
#             print("  Stop signal received, ending processing")
#             break
#         try:
#             if data_item.startswith("ERROR"):
#                 raise ValueError("Simulated processing error")
#             if data_item.startswith("SKIP"):
#                 print("  Item marked for skipping")
#                 continue
#             elif data_item.startswith("SPECIAL"):
#                 pass  # special items need no extra processing
#             else:
#                 print(f"  Processing: {data_item}")
#             processed_count += 1
#         except ValueError as e:
#             print(f"  Error processing {data_item}: {e}")
#             error_count += 1
#             continue
#     print(f"\nProcessing complete:")
#     print(f"  Successfully processed: {processed_count}")
#     print(f"  Errors encountered: {error_count}")
# test_data = [
#     "item1",
#     "SKIP_item2", 
#     "",
#     "ERROR_item3",
#     "SPECIAL_item4",
#     "item5",
#     "STOP",
#     "item6"  # this won't be processed due to STOP
# ]
# process_data_batch(test_data)

# Menu System Example:
# python
# class SimpleCalculator:
#     def run(self):
#         while True:
#             self.show_menu()
#             choice = input("Enter your choice: ").strip()
#             if choice == '5':
#                 print("Thank you for using the calculator!")
#                 break  # exit the program
#             if choice not in ['1', '2', '3', '4']:
#                 print("Invalid choice. Please try again.")
#                 continue  # show menu again
#             try:
#                 num1 = float(input("Enter first number: "))
#                 num2 = float(input("Enter second number: "))
#             except ValueError:
#                 print("Invalid input. Please enter valid numbers.")
#                 continue  # restart the loop
#             if choice == '1':
#                 result = num1 + num2
#                 operation = "addition"
#             elif choice == '2':
#                 result = num1 - num2
#                 operation = "subtraction"
#             elif choice == '3':
#                 result = num1 * num2
#                 operation = "multiplication"
#             elif choice == '4':
#                 if num2 == 0:
#                     print("Error: Division by zero!")
#                     continue  # restart the loop
#                 result = num1 / num2
#                 operation = "division"
#             else:
#                 pass  # this should never execute due to validation above
#             print(f"Result of {operation}: {result}")
#             print("-" * 30)
#     def show_menu(self):
#         print("\n=== Simple Calculator ===")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Exit")
# calculator = SimpleCalculator()
# calculator.run()