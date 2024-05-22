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

"""
Multi line comment
"""