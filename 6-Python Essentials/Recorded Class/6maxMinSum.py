li = [1, 3, 6, 10, 100, 14, 5, 9]

# print(max(li))

mx = float("-inf")
# print(mx)

for num in li:
    if (num > mx):
        mx = num

print(mx)


mn = float("inf")

for num in li:
    if (num < mn):
        mn = num

print(mn)

# res = sum(li)
res = 0
for num in li:
    res += num

print(res)