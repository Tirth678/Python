# usage of break, continue and pass statements
# pass is used to often leave space for another user to complete your code, or just leaving that space for future refereance
def factorial(x):
    if x == 0 or 1:
        return 1
    else:
        pass

# this is a space left for future someone else will complete, or I'll complete afterwards

# break is usally used to break out of any loop

for i in range(11):
    if i%5 == 0:
        print(i)
    if i%11 == 0:
        break