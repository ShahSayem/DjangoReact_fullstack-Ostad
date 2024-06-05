#Task:
#1.Factorial function using recursion
#fact(5) = 5*4*3*2*1

# n = int(input())

def fact(n):
    if (n <= 0):
        return 1
    
    return n*fact(n-1)

# print(fact(n))


#2. Reverse a string using recursion

str = input()
li = list(str)

sz = len(str)

def revStr(idx):
    if (idx < sz/2):
        li[idx], li[-1-idx] = li[-1-idx], li[idx]
        revStr(idx+1)

    return

# str = "-".join(li)
revStr(0)
print(li)


