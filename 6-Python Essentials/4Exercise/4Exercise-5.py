#Write a program to create a recursive function to calculate 
#the sum of numbers from 0 to n

n = int(input())

def recSum(n):
    if (n == 0):
        return 0
    
    return n+recSum(n-1)

print(recSum(n))

#Task:
#1.Factorial function using recursion
#fact(5) = 5*4*3*2*1

#2. Reverse a string using recursion




