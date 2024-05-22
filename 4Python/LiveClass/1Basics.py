print("Hey there!")

# Variables & Data types
a, b, s, x, y = 10.5, 20, 'Shah Sayem', True, False
c = a+b

print(c, s, x)
print(type(a), type(b), type(c), type(s), type(x))


# Arithmetic Operations
n1, n2 = 10, 4
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 // n2) #int portion of division
print(n1 % n2)
print(n1 ** n2) # n1 ^ n2


print(divmod(n1, n2)) # return (division, remender)
name = "Elon Musk"
marks = 80
grade = "A+"
cgpa = 3.6

print(type(name))

name = 30
print(type(name))


# Loops
n = 5
# n = int(input("Enter a number: "))
for _ in range(n):
    print("LOL under loop")
    print(_)
print("LOL outer loop \n")

          #start  end+1 increament
for i in range(1,    10,     2):
    print(i)

sum = 0
for i in range(1, 6):
    sum += i

print(sum, "\n")

for i in range(20, -1, -2):
    print(i)


# Functions
           #parameter
def greetings(name):
    pass #it means do nothing
    print(name, ",\nWelcome to the customer service.....")

           #argument
greetings("Shah Sayem") 

def add(a, b):
    return a+b

print("Sum of 2, 3 & 5 is:", add(add(3, 2), 5))

"""
Multi line comment
"""