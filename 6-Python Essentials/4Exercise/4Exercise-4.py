#Write a program to create function calculation() such that 
#it can accept two variable and calculates addition, substruction.
#Also it  must return both addition and substruction in a single return call.

def calculation(a, b):
    addition = a+b
    substruction = a-b

    return addition, substruction

print(calculation(10, 5))