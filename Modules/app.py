# from sales import Something
from sales import factorial
import sales
import sys
# agar koi folder me hai to to waha __init__.py add kro aur uske baad import folder_name.sales
# or better from folder_name.sales import something

# fact: jis bhi folder me hai wo package uss folder me __init__.py add krke from falana import dhikna
# dir function will return all details regarding package

# sales.factorial()
print(factorial(3))
print(sys.path) # system path
print(dir(sales))
print(sales.__name__)
print(sales.__package__)
