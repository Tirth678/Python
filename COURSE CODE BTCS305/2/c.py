# show replacement of switch statements
# replaceing switch statements is a good idea, but theoretically speaking switch often gets the job done

# if-else chaining
def handle_day(day):
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else:
        return "Invalid day"

print(handle_day(3))  # Output: Wednesday

# dictionary mapping
def get_day_name(day):
    days = {
        1: "Monday",
        2: "Tuesday", 
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(day, "Invalid day")

print(get_day_name(5))  # Output: Friday

# dictionary with functions
def monday_task():
    return "Start the week strong!"

def friday_task():
    return "TGIF!"

def weekend_task():
    return "Time to relax!"

def default_task():
    return "Regular day"

def execute_day_task(day):
    tasks = {
        1: monday_task,
        5: friday_task,
        6: weekend_task,
        7: weekend_task
    }
    task_function = tasks.get(day, default_task)
    return task_function()

print(execute_day_task(1))  # Output: Start the week strong!
print(execute_day_task(6))  # Output: Time to relax!

# lambda functions in dictionary
def calculate(operation, x, y):
    operations = {
        'add': lambda a, b: a + b,
        'subtract': lambda a, b: a - b,
        'multiply': lambda a, b: a * b,
        'divide': lambda a, b: a / b if b != 0 else "Cannot divide by zero"
    }
    return operations.get(operation, lambda a, b: "Invalid operation")(x, y)

print(calculate('add', 10, 5))      # Output: 15
print(calculate('multiply', 4, 3))  # Output: 12

# class-based approach
class StatusHandler:
    def handle_success(self):
        return "Operation completed successfully"
    
    def handle_error(self):
        return "An error occurred"
    
    def handle_warning(self):
        return "Warning: Check your input"
    
    def handle_default(self):
        return "Unknown status"
    
    def process_status(self, status_code):
        method_name = f"handle_{status_code}"
        method = getattr(self, method_name, self.handle_default)
        return method()

handler = StatusHandler()
print(handler.process_status('success'))  # Output: Operation completed successfully
print(handler.process_status('error'))    # Output: An error occurred

# match based statements
def handle_http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case status if 400 <= status < 500:
            return "Client Error"
        case status if 500 <= status < 600:
            return "Server Error"
        case _:
            return "Unknown Status"

print(handle_http_status(200))  # Output: OK
print(handle_http_status(403))  # Output: Client Error

# using advance search patterns
def process_data(data):
    match data:
        case {'type': 'user', 'name': str(name)}:
            return f"Processing user: {name}"
        case {'type': 'admin', 'permissions': list(perms)}:
            return f"Admin with permissions: {', '.join(perms)}"
        case {'type': 'guest'}:
            return "Processing guest user"
        case [first, *rest] if len(rest) > 0:
            return f"List starting with {first}, has {len(rest)} more items"
        case str(text) if len(text) > 10:
            return f"Long string: {text[:10]}..."
        case _:
            return "Unknown data format"

# Test cases
print(process_data({'type': 'user', 'name': 'Alice'}))
print(process_data(['apple', 'banana', 'cherry']))
print(process_data("This is a very long string"))