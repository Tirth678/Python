# prime number
n = int(input("Enter a number\n"))
if n<=1:
    print("Not prime\n")
else:
    for i in range(2,n):
        if n%i == 0:
            print("Not prime\n")
            break
    else:
        print("Prime\n")

# factorial
num = int(input("Enter a value\n"))
fact = 1
for i in range(1, num+1):
    fact *= i
print('factorial of', n, 'is', fact)

# fibonacci
a = int(input("Enter a value\n"))
b,c = 0,1
print("Fibonacci sequence: ")
for i in range(a):
    print(b, end="")
    a,b = b,a+b