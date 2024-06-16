#Touple - Immutable (String also immutable)
items = (1, 2, 3, 2, 2, 3)
print(type(items), items)

print(items.count(2))
print(items.index(2))
# print(dir(items)) 

a, b = 5, 10
temp = a
a = b
b = temp
print(a, b)


a, b = 2, 4
b, a = a, b
print(a, b)