#Count the total number of digits in a number

n = int(input())
cnt = 0

while (n):
    n = n//10
    cnt+=1
    # print(cnt, " ", n)

print(cnt)