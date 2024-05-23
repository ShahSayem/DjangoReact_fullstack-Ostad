# Conditionals 

# marks = int(input("Enter marks:"))
marks = 60

grade = ""

if (marks >= 80):
    grade = "A+"
elif (marks >= 70):
    grade = "A"
elif (marks >= 60):
    grade = "A-"
elif (marks >= 50):
    grade = "B"
elif (marks >= 40):
    grade = "C"
elif (marks >= 33):
    grade = "D"
else:
    grade = "F"

print("Grade is:", grade)
print("\n")


# n = int(input("Enter a number:"))
n = -4

if (n >= 0 and n%2):
        print(n, "is a positive & odd number")
elif (n >= 0 and n%2 == 0):
        print(n, "is a positive & even number")
elif (n < 0 and n%2):
        print(n, "is a negative & odd number")
else:
        print(n, "is a negative & even number")
print("\n")



def leapYearChecker(year):
    if (year%400 == 0):
        print(year, "is leap year")
    elif (year%100 and year%4 == 0):
        print(year, "is leap year")
    else:
         pass
        # print(year, "is not leap year")


# year = int(input("Enter a year:"))
for i in range (1900, 2025):
    leapYearChecker(i)
print("\n")

"""
Multi line comment
"""

# List 
fruits = ["apple", "orange", "mango"]
print(fruits[2])

fruits.append("Banana")
print(len(fruits))

print("Papaya" in fruits)

fruits.pop()
print(fruits)
print("\n")


# Loop 
for curr in fruits:
    print(curr)
print("\n")

i = 1
while (i <= 5):
    print(i)
    i += 1
print("\n")



# Function 
def mulTable(n):
    for i in range(1, 11):
        # print(n, "X", i, "=", n*i)
        print("{} X {} = {}".format(n, i, n*i))

n = 1
while (n):
    mulTable(n)
    n = int (input("Enter a number for mulTable or 0 to exit:"))

print("\n")


#Library function
import random
import datetime
import math

randNum = random.randint(1, 100)
print(randNum)

today = datetime.datetime.today()
print(today)

x = math.sqrt(100)
print(x)

pi = math.pi
print(pi)
print("\n")


# String 
lols = ["10"+"10", "10"*3]

print(lols)
print(len(lols[0]))
print(lols[0][0:2])

s = "abcd"
print(s[0])
print(s[-1])
print(s[-2])
print(s[-2:])
print(s[:])

name = "srk"
name = name.upper()
print(name)

person = "ELON MUSK"
# person = person.lower()
person = person.capitalize()
print(person)

# person[0] = "B" //Doesn't work as string is immuteable

# idx = "Bangladesh".find("Bangla") #0
# idx = "Bangladesh".find("desh")  #6 
country = "Bangladesh"
idx = country.find("gcd")  #-1 
print(idx)

print(country.startswith("xyz"))
print(country.endswith("desh"))

str = "A, B, C, D"
temp = str.split(",")
print(temp)

li = ["a", "b", "c"]
x = ",".join(li)
print(x)

