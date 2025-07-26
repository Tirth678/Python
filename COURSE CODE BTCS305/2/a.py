# conditional statements

x = int(input("Enter your age\n"))
if x >= 18:
    print("You are eligible to vote!\n")
elif x < 18:
    print("You are not elgible to vote!\n")
else:
    print("Please enter a valid value to continue")

# Simple if statement
age = 18
print(f"Age: {age}")

if age >= 18:
    print("✓ You are eligible to vote!")
    print("✓ You can apply for a driver's license!")

# Multiple conditions in if
temperature = 25
print(f"\nTemperature: {temperature}°C")

if temperature > 30:
    print("It's hot outside!")

if temperature >= 20 and temperature <= 30:
    print("Perfect weather!")

if temperature < 20:
    print("It's cool outside!")

# Boolean variable in if
is_raining = True
has_umbrella = False

print(f"\nIs raining: {is_raining}")
print(f"Has umbrella: {has_umbrella}")

if is_raining:
    print("It's raining!")
    if has_umbrella:
        print("You can go out with your umbrella.")
    else:
        print("Better stay inside or get an umbrella.")

# 2. IF-ELSE STATEMENT
print("\n\n2. IF-ELSE STATEMENT")
print("-" * 40)

# Basic if-else
number = 15
print(f"Number: {number}")

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Password strength checker
password = "MySecure123"
print(f"\nPassword: '{password}'")

if len(password) >= 8:
    print("✓ Password is strong enough")
else:
    print("✗ Password is too short (minimum 8 characters)")

# Login system example
username = "admin"
user_password = "admin123"
correct_username = "admin"
correct_password = "admin123"

print(f"\nLogin attempt:")
print(f"Username: {username}")
print(f"Password: {user_password}")

if username == correct_username and user_password == correct_password:
    print("✓ Login successful! Welcome!")
else:
    print("✗ Invalid credentials. Access denied.")

# 3. IF-ELIF-ELSE STATEMENT
print("\n\n3. IF-ELIF-ELSE STATEMENT")
print("-" * 40)

# Grade calculator
score = 85
print(f"Student score: {score}")

if score >= 90:
    grade = "A"
    status = "Excellent"
elif score >= 80:
    grade = "B"
    status = "Good"
elif score >= 70:
    grade = "C"
    status = "Average"
elif score >= 60:
    grade = "D"
    status = "Below Average"
else:
    grade = "F"
    status = "Fail"

print(f"Grade: {grade}")
print(f"Status: {status}")

# Traffic light system
light_color = "yellow"
print(f"\nTraffic light: {light_color}")

if light_color == "red":
    action = "STOP"
    description = "Do not proceed"
elif light_color == "yellow":
    action = "CAUTION"
    description = "Prepare to stop"
elif light_color == "green":
    action = "GO"
    description = "Proceed safely"
else:
    action = "ERROR"
    description = "Invalid light color"

print(f"Action: {action}")
print(f"Description: {description}")

# BMI Calculator
weight = 70  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)

print(f"\nBMI Calculator:")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    category = "Underweight"
    recommendation = "Consider gaining weight"
elif bmi < 25:
    category = "Normal weight"
    recommendation = "Maintain current weight"
elif bmi < 30:
    category = "Overweight"
    recommendation = "Consider losing weight"
else:
    category = "Obese"
    recommendation = "Consult a healthcare provider"

print(f"Category: {category}")
print(f"Recommendation: {recommendation}")

# 4. NESTED CONDITIONAL STATEMENTS
print("\n\n4. NESTED CONDITIONAL STATEMENTS")
print("-" * 40)

# Admission eligibility checker
math_score = 85
science_score = 78
english_score = 88
total_score = math_score + science_score + english_score
average_score = total_score / 3

print(f"Admission Eligibility Checker:")
print(f"Math: {math_score}, Science: {science_score}, English: {english_score}")
print(f"Total: {total_score}, Average: {average_score:.1f}")

if average_score >= 75:
    print("✓ Average score requirement met")
    
    if math_score >= 70 and science_score >= 70:
        print("✓ Core subjects requirement met")
        
        if english_score >= 80:
            print("✓ Language requirement met")
            print("🎉 ADMISSION GRANTED - Premium Program")
        else:
            print("✓ Basic language requirement met")
            print("✅ ADMISSION GRANTED - Standard Program")
    else:
        print("✗ Core subjects requirement not met")
        print("❌ ADMISSION DENIED")
else:
    print("✗ Average score requirement not met")
    print("❌ ADMISSION DENIED")

# Weather-based activity planner
weather = "sunny"
temperature_today = 28
has_free_time = True

print(f"\nActivity Planner:")
print(f"Weather: {weather}")
print(f"Temperature: {temperature_today}°C")
print(f"Free time available: {has_free_time}")

if has_free_time:
    print("You have free time!")
    
    if weather == "sunny":
        if temperature_today > 25:
            print("🌞 Perfect for outdoor activities!")
            print("Suggestions: Swimming, hiking, picnic")
        else:
            print("🌤️ Good for mild outdoor activities")
            print("Suggestions: Walking, cycling, photography")
    elif weather == "rainy":
        print("🌧️ Indoor activities recommended")
        print("Suggestions: Reading, movies, cooking")
    else:
        print("🌤️ Check weather and plan accordingly")
else:
    print("No free time available. Focus on your tasks!")

# 5. LOGICAL OPERATORS IN CONDITIONS
print("\n\n5. LOGICAL OPERATORS IN CONDITIONS")
print("-" * 40)

# AND operator examples
user_age = 25
has_license = True
has_insurance = True
has_car = False

print(f"Driving Eligibility Check:")
print(f"Age: {user_age}, License: {has_license}, Insurance: {has_insurance}, Car: {has_car}")

if user_age >= 18 and has_license and has_insurance:
    print("✓ Legally eligible to drive")
    if has_car:
        print("✓ Can drive own car")
    else:
        print("⚠️ Needs to rent or borrow a car")
else:
    print("✗ Not eligible to drive")

# OR operator examples
payment_method = "credit_card"
account_balance = 50
credit_limit = 1000

print(f"\nPayment Processing:")
print(f"Method: {payment_method}, Balance: ${account_balance}, Credit: ${credit_limit}")

if payment_method == "cash" or account_balance >= 100 or credit_limit >= 500:
    print("✓ Payment can be processed")
else:
    print("✗ Payment declined - insufficient funds/credit")

# NOT operator examples
is_weekend = False
is_holiday = False
is_sick = False

print(f"\nWork Day Check:")
print(f"Weekend: {is_weekend}, Holiday: {is_holiday}, Sick: {is_sick}")

if not is_weekend and not is_holiday and not is_sick:
    print("📅 Regular work day - go to office")
else:
    if is_weekend:
        print("🎉 It's weekend - enjoy!")
    elif is_holiday:
        print("🎊 It's a holiday - relax!")
    elif is_sick:
        print("🤒 Take rest and recover")

# 6. MEMBERSHIP AND IDENTITY OPERATORS
print("\n\n6. MEMBERSHIP AND IDENTITY OPERATORS")
print("-" * 40)

# IN operator
valid_grades = ['A', 'B', 'C', 'D', 'F']
student_grade = 'B'

print(f"Grade validation:")
print(f"Valid grades: {valid_grades}")
print(f"Student grade: {student_grade}")

if student_grade in valid_grades:
    print("✓ Valid grade entered")
else:
    print("✗ Invalid grade")

# String membership
email = "user@example.com"
domain_whitelist = ["gmail.com", "yahoo.com", "example.com"]

print(f"\nEmail validation:")
print(f"Email: {email}")
print(f"Allowed domains: {domain_whitelist}")

email_domain = email.split('@')[1] if '@' in email else ""
if email_domain in domain_whitelist:
    print("✓ Email domain is allowed")
else:
    print("✗ Email domain not allowed")

# IS operator (identity)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"\nIdentity checking:")
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3 = list1")

if list1 is list3:
    print("list1 is list3: Same object")
else:
    print("list1 is not list3: Different objects")

if list1 is list2:
    print("list1 is list2: Same object")
else:
    print("list1 is not list2: Different objects (but same content)")

# 7. TERNARY OPERATOR (CONDITIONAL EXPRESSION)
print("\n\n7. TERNARY OPERATOR (CONDITIONAL EXPRESSION)")
print("-" * 40)

# Basic ternary operator
age_check = 20
status = "Adult" if age_check >= 18 else "Minor"
print(f"Age: {age_check}, Status: {status}")

# Multiple ternary operators
temperature_check = 35
weather_desc = "Hot" if temperature_check > 30 else "Warm" if temperature_check > 20 else "Cool"
print(f"Temperature: {temperature_check}°C, Description: {weather_desc}")

# Ternary in function calls
numbers = [1, 2, 3, 4, 5]
result = max(numbers) if numbers else 0
print(f"Numbers: {numbers}, Max value: {result}")

# Ternary for default values
username_input = ""
display_name = username_input if username_input else "Guest User"
print(f"Input: '{username_input}', Display: '{display_name}'")

# 8. PRACTICAL APPLICATIONS
print("\n\n8. PRACTICAL APPLICATIONS")
print("-" * 40)

# Example 1: E-commerce Discount Calculator
def calculate_discount(purchase_amount, customer_type, is_first_purchase):
    print(f"Purchase Amount: ${purchase_amount}")
    print(f"Customer Type: {customer_type}")
    print(f"First Purchase: {is_first_purchase}")
    
    discount = 0
    
    if is_first_purchase:
        discount = 10  # 10% for first purchase
        print("✓ First purchase bonus: 10%")
    
    if customer_type == "premium":
        discount += 15  # Additional 15% for premium
        print("✓ Premium customer bonus: 15%")
    elif customer_type == "gold":
        discount += 10  # Additional 10% for gold
        print("✓ Gold customer bonus: 10%")
    elif customer_type == "silver":
        discount += 5   # Additional 5% for silver
        print("✓ Silver customer bonus: 5%")
    
    if purchase_amount > 1000:
        discount += 5   # Additional 5% for large purchases
        print("✓ Large purchase bonus: 5%")
    
    # Cap discount at 50%
    discount = min(discount, 50)
    discount_amount = purchase_amount * (discount / 100)
    final_amount = purchase_amount - discount_amount
    
    print(f"Total Discount: {discount}%")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Final Amount: ${final_amount:.2f}")
    return final_amount

print("=== E-COMMERCE DISCOUNT CALCULATOR ===")
calculate_discount(1200, "premium", True)

# Example 2: Bank Loan Eligibility
print("\n=== BANK LOAN ELIGIBILITY CHECKER ===")

def check_loan_eligibility(age, income, credit_score, employment_years, existing_loans):
    print(f"Applicant Details:")
    print(f"Age: {age}")
    print(f"Annual Income: ${income:,}")
    print(f"Credit Score: {credit_score}")
    print(f"Employment Years: {employment_years}")
    print(f"Existing Loans: ${existing_loans:,}")
    
    eligible = True
    reasons = []
    loan_amount = 0
    interest_rate = 0
    
    # Age requirement
    if age < 21 or age > 65:
        eligible = False
        reasons.append("Age must be between 21-65")
    
    # Income requirement
    if income < 30000:
        eligible = False
        reasons.append("Minimum income requirement: $30,000")
    
    # Credit score requirement
    if credit_score < 600:
        eligible = False
        reasons.append("Minimum credit score: 600")
    
    # Employment requirement
    if employment_years < 2:
        eligible = False
        reasons.append("Minimum employment: 2 years")
    
    # Debt-to-income ratio
    debt_ratio = (existing_loans / income) * 100
    if debt_ratio > 40:
        eligible = False
        reasons.append(f"Debt-to-income ratio too high: {debt_ratio:.1f}% (max 40%)")
    
    if eligible:
        # Calculate loan amount and interest rate
        if credit_score >= 750:
            loan_amount = income * 10
            interest_rate = 3.5
        elif credit_score >= 700:
            loan_amount = income * 8
            interest_rate = 4.0
        else:
            loan_amount = income * 6
            interest_rate = 4.5
        
        print("\n✅ LOAN APPROVED!")
        print(f"Maximum Loan Amount: ${loan_amount:,}")
        print(f"Interest Rate: {interest_rate}%")
    else:
        print("\n❌ LOAN REJECTED!")
        print("Reasons:")
        for reason in reasons:
            print(f"  • {reason}")

check_loan_eligibility(35, 75000, 720, 5, 15000)

# Example 3: Student Grade Management System
print("\n=== STUDENT GRADE MANAGEMENT SYSTEM ===")

def process_student_grades(name, scores):
    print(f"Student: {name}")
    print(f"Scores: {scores}")
    
    if not scores:
        print("No scores available")
        return
    
    total = sum(scores)
    average = total / len(scores)
    
    # Determine letter grade
    if average >= 97:
        letter_grade = "A+"
        gpa = 4.0
    elif average >= 93:
        letter_grade = "A"
        gpa = 4.0
    elif average >= 90:
        letter_grade = "A-"
        gpa = 3.7
    elif average >= 87:
        letter_grade = "B+"
        gpa = 3.3
    elif average >= 83:
        letter_grade = "B"
        gpa = 3.0
    elif average >= 80:
        letter_grade = "B-"
        gpa = 2.7
    elif average >= 77:
        letter_grade = "C+"
        gpa = 2.3
    elif average >= 73:
        letter_grade = "C"
        gpa = 2.0
    elif average >= 70:
        letter_grade = "C-"
        gpa = 1.7
    elif average >= 67:
        letter_grade = "D+"
        gpa = 1.3
    elif average >= 65:
        letter_grade = "D"
        gpa = 1.0
    else:
        letter_grade = "F"
        gpa = 0.0
    
    # Determine status and recommendations
    if average >= 95:
        status = "Excellent - Honor Roll"
        recommendation = "Continue outstanding work!"
    elif average >= 85:
        status = "Good - Above Average"
        recommendation = "Great job! Keep it up!"
    elif average >= 75:
        status = "Satisfactory - Average"
        recommendation = "Good work, room for improvement"
    elif average >= 65:
        status = "Below Average - Needs Improvement"
        recommendation = "Focus on weak areas, seek help"
    else:
        status = "Failing - Immediate Action Required"
        recommendation = "Meet with advisor immediately"
    
    print(f"\nResults:")
    print(f"Total Points: {total}")
    print(f"Average: {average:.1f}%")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa}")
    print(f"Status: {status}")
    print(f"Recommendation: {recommendation}")

process_student_grades("Alice Johnson", [92, 88, 95, 87, 91])

# 9. BEST PRACTICES AND COMMON PATTERNS
print("\n\n9. BEST PRACTICES AND COMMON PATTERNS")
print("-" * 40)

print("""
CONDITIONAL STATEMENTS BEST PRACTICES:

1. USE CLEAR CONDITIONS:
   ✓ if temperature > 30:
   ✗ if temp > 30:  # unclear variable name

2. AVOID DEEPLY NESTED CONDITIONS:
   ✓ Use early returns or guard clauses
   ✗ if condition1:
         if condition2:
             if condition3:  # too nested

3. USE LOGICAL OPERATORS EFFICIENTLY:
   ✓ if 18 <= age <= 65:
   ✗ if age >= 18 and age <= 65:

4. HANDLE EDGE CASES:
   ✓ Always consider None, empty strings, zero values
   
5. USE TERNARY OPERATORS FOR SIMPLE CONDITIONS:
   ✓ status = "pass" if score >= 60 else "fail"
   
6. GROUP RELATED CONDITIONS:
   ✓ Use elif instead of multiple if statements when appropriate

7. USE MEANINGFUL VARIABLE NAMES:
   ✓ is_valid, has_permission, can_proceed
   ✗ flag, check, temp

8. VALIDATE INPUT DATA:
   ✓ Always check for valid ranges and types
""")

# 10. COMMON CONDITIONAL PATTERNS
print("\n\n10. COMMON CONDITIONAL PATTERNS")
print("-" * 40)

# Pattern 1: Guard Clauses
def process_user_data(user_data):
    print("Processing user data with guard clauses:")
    
    # Guard clauses - early returns
    if not user_data:
        print("✗ No data provided")
        return
    
    if 'name' not in user_data:
        print("✗ Name is required")
        return
    
    if 'age' not in user_data:
        print("✗ Age is required")
        return
    
    # Main processing logic
    print(f"✓ Processing user: {user_data['name']}, Age: {user_data['age']}")

process_user_data({'name': 'John', 'age': 25})

# Pattern 2: State Machine
def traffic_light_controller(current_state, action):
    print(f"Traffic Light State Machine:")
    print(f"Current state: {current_state}, Action: {action}")
    
    if current_state == "red":
        if action == "timer_expired":
            next_state = "green"
        else:
            next_state = "red"
    elif current_state == "green":
        if action == "timer_expired":
            next_state = "yellow"
        else:
            next_state = "green"
    elif current_state == "yellow":
        if action == "timer_expired":
            next_state = "red"
        else:
            next_state = "yellow"
    else:
        next_state = "red"  # Default state
    
    print(f"Next state: {next_state}")
    return next_state

traffic_light_controller("red", "timer_expired")

print("\n" + "=" * 70)
print("CONDITIONAL STATEMENTS DEMONSTRATION COMPLETE")
print("=" * 70)

# Summary
print("\nSUMMARY OF CONDITIONAL STATEMENTS:")
print("✓ if statement - single condition")
print("✓ if-else statement - two-way branching")
print("✓ if-elif-else statement - multi-way branching")
print("✓ Nested conditions - conditions within conditions")
print("✓ Logical operators - and, or, not")
print("✓ Membership operators - in, not in")
print("✓ Identity operators - is, is not")
print("✓ Ternary operator - conditional expressions")
print("✓ Practical applications and best practices")