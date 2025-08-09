class Something:
    def __init__(self):
        pass
    def hello(self, str):
        return self
    
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
            