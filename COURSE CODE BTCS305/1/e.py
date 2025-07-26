# there is no such concept of declearing contants in python but we do have some methods, to decleare variables as 
# contatns.
# we can decleare variables in capital letters as defining a macro in C/C++
# it is very different here in python, but to keep it simple and easy to read
INT_DATA = 12
print(INT_DATA)


# Mathematical constants
PI = 3.14159265359
E = 2.71828182846
GOLDEN_RATIO = 1.61803398875

# Application constants
MAX_USERS = 1000
MIN_PASSWORD_LENGTH = 8
DEFAULT_TIMEOUT = 30
APP_VERSION = "1.2.3"

# Configuration constants
DEBUG_MODE = True
DATABASE_URL = "localhost:5432"
SECRET_KEY = "your-secret-key-here"

print(f"Mathematical Constants:")
print(f"PI = {PI}")
print(f"E = {E}")
print(f"GOLDEN_RATIO = {GOLDEN_RATIO}")

print(f"\nApplication Constants:")
print(f"MAX_USERS = {MAX_USERS}")
print(f"MIN_PASSWORD_LENGTH = {MIN_PASSWORD_LENGTH}")
print(f"DEFAULT_TIMEOUT = {DEFAULT_TIMEOUT}")
print(f"APP_VERSION = {APP_VERSION}")

print(f"\nConfiguration Constants:")
print(f"DEBUG_MODE = {DEBUG_MODE}")
print(f"DATABASE_URL = {DATABASE_URL}")
print(f"SECRET_KEY = {SECRET_KEY}")

# 2. CONSTANTS IN CALCULATIONS
print("\n\n2. USING CONSTANTS IN CALCULATIONS")
print("-" * 40)

# Circle calculations using PI
radius = 5
area = PI * radius ** 2
circumference = 2 * PI * radius
volume_sphere = (4/3) * PI * radius ** 3

print(f"Circle Calculations (radius = {radius}):")
print(f"Area = π × r² = {PI} × {radius}² = {area:.2f}")
print(f"Circumference = 2 × π × r = 2 × {PI} × {radius} = {circumference:.2f}")
print(f"Sphere Volume = (4/3) × π × r³ = {volume_sphere:.2f}")

# Compound interest calculation using E
principal = 1000
rate = 0.05
time = 10
compound_interest = principal * (E ** (rate * time))
print(f"\nCompound Interest Calculation:")
print(f"Principal: ${principal}, Rate: {rate*100}%, Time: {time} years")
print(f"Amount = P × e^(rt) = ${compound_interest:.2f}")

# 3. CONSTANTS ORGANIZATION WITH CLASSES
print("\n\n3. ORGANIZING CONSTANTS WITH CLASSES")
print("-" * 40)

class MathConstants:
    """Mathematical constants"""
    PI = 3.141592653589793
    E = 2.718281828459045
    TAU = 2 * PI  # Full circle in radians
    PHI = 1.618033988749  # Golden ratio
    SQRT_2 = 1.4142135623730951

class PhysicsConstants:
    """Physical constants"""
    SPEED_OF_LIGHT = 299792458  # m/s
    GRAVITY = 9.80665  # m/s²
    PLANCK_CONSTANT = 6.62607015e-34  # J⋅s
    BOLTZMANN_CONSTANT = 1.380649e-23  # J/K
    AVOGADRO_NUMBER = 6.02214076e23  # mol⁻¹

class AppConfig:
    """Application configuration constants"""
    MAX_LOGIN_ATTEMPTS = 3
    SESSION_TIMEOUT = 1800  # 30 minutes in seconds
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_FILE_TYPES = ['.jpg', '.png', '.pdf', '.doc']
    CACHE_DURATION = 3600  # 1 hour

# Using class-based constants
print("Math Constants:")
print(f"PI = {MathConstants.PI}")
print(f"TAU = {MathConstants.TAU}")
print(f"Golden Ratio = {MathConstants.PHI}")

print("\nPhysics Constants:")
print(f"Speed of Light = {PhysicsConstants.SPEED_OF_LIGHT:,} m/s")
print(f"Gravity = {PhysicsConstants.GRAVITY} m/s²")

print("\nApp Configuration:")
print(f"Max Login Attempts = {AppConfig.MAX_LOGIN_ATTEMPTS}")
print(f"Session Timeout = {AppConfig.SESSION_TIMEOUT} seconds")
print(f"Max File Size = {AppConfig.MAX_FILE_SIZE:,} bytes")

# 4. CONSTANTS WITH ENUM
print("\n\n4. CONSTANTS WITH ENUM")
print("-" * 40)

from enum import Enum, IntEnum

class Status(Enum):
    """Order status constants"""
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Priority(IntEnum):
    """Priority levels with integer values"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

class Colors(Enum):
    """Color constants with hex values"""
    RED = "#FF0000"
    GREEN = "#00FF00"
    BLUE = "#0000FF"
    YELLOW = "#FFFF00"
    WHITE = "#FFFFFF"
    BLACK = "#000000"

# Using enum constants
current_status = Status.PROCESSING
task_priority = Priority.HIGH
theme_color = Colors.BLUE

print("Enum Constants:")
print(f"Order Status: {current_status.value}")
print(f"Task Priority: {task_priority.value}")
print(f"Theme Color: {theme_color.value}")

# Enum comparison and iteration
print(f"\nEnum Operations:")
print(f"High priority > Medium priority: {Priority.HIGH > Priority.MEDIUM}")
print(f"All status options: {[status.value for status in Status]}")

# 5. IMMUTABLE CONSTANTS WITH NAMEDTUPLE
print("\n\n5. IMMUTABLE CONSTANTS WITH NAMEDTUPLE")
print("-" * 40)

from collections import namedtuple

# Create namedtuple types for constants
DatabaseConfig = namedtuple('DatabaseConfig', [
    'HOST', 'PORT', 'NAME', 'USER', 'PASSWORD', 'TIMEOUT'
])

APIConfig = namedtuple('APIConfig', [
    'BASE_URL', 'VERSION', 'TIMEOUT', 'MAX_RETRIES', 'API_KEY'
])

# Create constant instances
DB_CONFIG = DatabaseConfig(
    HOST='localhost',
    PORT=5432,
    NAME='myapp_db',
    USER='admin',
    PASSWORD='secret123',
    TIMEOUT=30
)

API_CONFIG = APIConfig(
    BASE_URL='https://api.example.com',
    VERSION='v2',
    TIMEOUT=10,
    MAX_RETRIES=3,
    API_KEY='your-api-key'
)

print("Database Configuration:")
print(f"Host: {DB_CONFIG.HOST}")
print(f"Port: {DB_CONFIG.PORT}")
print(f"Database: {DB_CONFIG.NAME}")
print(f"Timeout: {DB_CONFIG.TIMEOUT}s")

print("\nAPI Configuration:")
print(f"Base URL: {API_CONFIG.BASE_URL}")
print(f"Version: {API_CONFIG.VERSION}")
print(f"Max Retries: {API_CONFIG.MAX_RETRIES}")

# Demonstrate immutability
print("\nTesting Immutability:")
try:
    DB_CONFIG.HOST = "newhost"
except AttributeError as e:
    print(f"✓ Cannot modify namedtuple: {e}")

# 6. FROZEN DATACLASS CONSTANTS
print("\n\n6. FROZEN DATACLASS CONSTANTS")
print("-" * 40)

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ServerConfig:
    """Immutable server configuration"""
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    WORKERS: int = 4
    ALLOWED_HOSTS: List[str] = None
    
    def __post_init__(self):
        if self.ALLOWED_HOSTS is None:
            object.__setattr__(self, 'ALLOWED_HOSTS', ['localhost', '127.0.0.1'])

@dataclass(frozen=True)
class SecurityConfig:
    """Immutable security configuration"""
    JWT_SECRET: str = "jwt-secret-key"
    JWT_EXPIRY: int = 3600
    BCRYPT_ROUNDS: int = 12
    RATE_LIMIT: int = 100
    CORS_ORIGINS: List[str] = None
    
    def __post_init__(self):
        if self.CORS_ORIGINS is None:
            object.__setattr__(self, 'CORS_ORIGINS', ['http://localhost:3000'])

# Create frozen instances
SERVER_CONFIG = ServerConfig()
SECURITY_CONFIG = SecurityConfig(JWT_EXPIRY=7200)  # Custom expiry

print("Server Configuration:")
print(f"Host: {SERVER_CONFIG.HOST}")
print(f"Port: {SERVER_CONFIG.PORT}")
print(f"Workers: {SERVER_CONFIG.WORKERS}")
print(f"Allowed Hosts: {SERVER_CONFIG.ALLOWED_HOSTS}")

print("\nSecurity Configuration:")
print(f"JWT Expiry: {SECURITY_CONFIG.JWT_EXPIRY}s")
print(f"BCrypt Rounds: {SECURITY_CONFIG.BCRYPT_ROUNDS}")
print(f"Rate Limit: {SECURITY_CONFIG.RATE_LIMIT}")

# Test immutability
print("\nTesting Frozen Dataclass:")
try:
    SERVER_CONFIG.PORT = 9000
except Exception as e:
    print(f"✓ Cannot modify frozen dataclass: {type(e).__name__}")

# 7. CONSTANTS IN REAL-WORLD SCENARIOS
print("\n\n7. REAL-WORLD CONSTANT USAGE")
print("-" * 40)

# File processing constants
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
CHUNK_SIZE = 8192  # 8KB chunks
SUPPORTED_FORMATS = ['.txt', '.csv', '.json', '.xml']

def process_file(filename, file_size):
    """Example function using constants"""
    if file_size > MAX_FILE_SIZE:
        return f"Error: File too large (max {MAX_FILE_SIZE:,} bytes)"
    
    file_ext = filename[filename.rfind('.'):]
    if file_ext not in SUPPORTED_FORMATS:
        return f"Error: Unsupported format (supported: {SUPPORTED_FORMATS})"
    
    chunks_needed = (file_size + CHUNK_SIZE - 1) // CHUNK_SIZE
    return f"Processing {filename}: {chunks_needed} chunks of {CHUNK_SIZE} bytes"

# Test file processing
test_files = [
    ("document.txt", 1024),
    ("data.csv", 30 * 1024 * 1024),  # 30MB
    ("image.jpg", 100 * 1024 * 1024),  # 100MB - too large
    ("config.xml", 512)
]

print("File Processing Results:")
for filename, size in test_files:
    result = process_file(filename, size)
    print(f"  {result}")

# 8. CONSTANT VALIDATION AND ERROR HANDLING
print("\n\n8. CONSTANT VALIDATION")
print("-" * 40)

# Validation functions for constants
def validate_constants():
    """Validate that constants have appropriate values"""
    errors = []
    
    if MAX_USERS <= 0:
        errors.append("MAX_USERS must be positive")
    
    if MIN_PASSWORD_LENGTH < 6:
        errors.append("MIN_PASSWORD_LENGTH too weak (minimum 6)")
    
    if DEFAULT_TIMEOUT <= 0:
        errors.append("DEFAULT_TIMEOUT must be positive")
    
    if not isinstance(APP_VERSION, str):
        errors.append("APP_VERSION must be a string")
    
    return errors

# Run validation
validation_errors = validate_constants()
if validation_errors:
    print("Validation Errors:")
    for error in validation_errors:
        print(f"  ✗ {error}")
else:
    print("✓ All constants are valid")

# 9. CONSTANTS WITH CALCULATIONS
print("\n\n9. DERIVED CONSTANTS")
print("-" * 40)

# Base constants
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
DAYS_PER_WEEK = 7

# Derived constants
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR
SECONDS_PER_DAY = SECONDS_PER_HOUR * HOURS_PER_DAY
SECONDS_PER_WEEK = SECONDS_PER_DAY * DAYS_PER_WEEK

# Memory size constants
BYTES_PER_KB = 1024
BYTES_PER_MB = BYTES_PER_KB * 1024
BYTES_PER_GB = BYTES_PER_MB * 1024

print("Time Constants:")
print(f"Seconds per hour: {SECONDS_PER_HOUR:,}")
print(f"Seconds per day: {SECONDS_PER_DAY:,}")
print(f"Seconds per week: {SECONDS_PER_WEEK:,}")

print("\nMemory Constants:")
print(f"Bytes per MB: {BYTES_PER_MB:,}")
print(f"Bytes per GB: {BYTES_PER_GB:,}")

# 10. BEST PRACTICES DEMONSTRATION
print("\n\n10. CONSTANTS BEST PRACTICES")
print("-" * 40)

# Good practices
class BestPractices:
    # 1. Use descriptive names
    MAX_RETRY_ATTEMPTS = 3  # Good
    # MAX_RETRIES = 3       # Less descriptive
    
    # 2. Group related constants
    # Database settings
    DB_HOST = "localhost"
    DB_PORT = 5432
    DB_NAME = "myapp"
    
    # Cache settings  
    CACHE_TTL = 3600
    CACHE_MAX_SIZE = 1000
    
    # 3. Use appropriate data types
    PI_PRECISE = 3.141592653589793  # Full precision
    MAX_INT = 2**31 - 1            # Clear calculation
    
    # 4. Include units in names when applicable
    TIMEOUT_SECONDS = 30
    MAX_SIZE_BYTES = 1024 * 1024
    RATE_LIMIT_PER_MINUTE = 100

# Usage examples
def connect_database():
    return f"Connecting to {BestPractices.DB_HOST}:{BestPractices.DB_PORT}/{BestPractices.DB_NAME}"

def calculate_circle_area(radius):
    return BestPractices.PI_PRECISE * radius ** 2

print("Best Practices Examples:")
print(f"Database connection: {connect_database()}")
print(f"Circle area (r=3): {calculate_circle_area(3):.6f}")
print(f"Timeout setting: {BestPractices.TIMEOUT_SECONDS} seconds")

# 11. CONSTANTS FILE STRUCTURE EXAMPLE
print("\n\n11. CONSTANTS FILE ORGANIZATION")
print("-" * 40)

print("""
Recommended constants.py file structure:

# constants.py
'''Application Constants'''

# Application Information
APP_NAME = "My Application"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "A sample application"

# Server Configuration
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8000
MAX_CONNECTIONS = 100

# Database Configuration
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "myapp_db"
DB_POOL_SIZE = 10

# Security Settings
JWT_SECRET_KEY = "your-jwt-secret"
JWT_EXPIRY_HOURS = 24
BCRYPT_ROUNDS = 12

# File Handling
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = ['.jpg', '.png', '.pdf']
UPLOAD_FOLDER = '/uploads'

# Cache Settings
CACHE_TTL = 3600  # 1 hour
CACHE_MAX_ENTRIES = 1000

# API Settings
API_RATE_LIMIT = 100  # requests per minute
API_TIMEOUT = 30  # seconds

Usage in other files:
from constants import APP_NAME, DEFAULT_PORT, MAX_UPLOAD_SIZE
""")

print("\n" + "=" * 70)
print("CONSTANTS WORKING DEMONSTRATION COMPLETE")
print("=" * 70)

# Summary of key points
print("\nKEY TAKEAWAYS:")
print("1. Use ALL_CAPS for constant names (convention)")
print("2. Group related constants in classes or modules")
print("3. Use Enum for related constant values")
print("4. Use frozen dataclass/namedtuple for true immutability")
print("5. Validate constants at application startup")
print("6. Use descriptive names with units when applicable")
print("7. Organize constants in dedicated files for large projects")
print("8. Document the purpose and valid ranges of constants")