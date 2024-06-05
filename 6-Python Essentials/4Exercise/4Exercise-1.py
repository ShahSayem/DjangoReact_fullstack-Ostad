#Write a program to print the following number pattern using a loop

# 1
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input())
for outer in range (1 ,n+1):
    li = []
    for inner in range (1, outer+1):
        print(inner, end=" ")
    print()

