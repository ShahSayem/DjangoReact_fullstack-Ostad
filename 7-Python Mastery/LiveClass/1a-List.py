# List - Mutable
items = []
items.append(1)
items.append(2)
items.append("Hello")
items.append([1, 2, 3])

print(items[0])
print(items[-1])

# for item in items:
#     print(item, type(item))4

# for i in range(0, len(items)):
#     print(i, items[i])
 
for i, item in enumerate(items):
    print(i, item)


li2 = [4, 10, 6, 2]

# items += li2
# print(items)

items.extend(li2)
print(items)

items.append(li2)
print(items)
print(len(items))
print(items[8][1])


li2Copy = li2.copy()
# li2Copy.sort()
li2Copy.sort(reverse=True)
print(li2Copy)

# print(dir(items))

# print(help(list.pop))

# x = li2.pop()
# print(x, "removed. Now:" ,li2)
      #idx 
li2.pop(1) 
print(li2)