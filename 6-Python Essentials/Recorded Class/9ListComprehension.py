li = ["aplle", "banana", "mango", "orange"]
fruits = [fruit.capitalize() for fruit in li]
print(fruits)

liLen = [len(x) for x in li]
print(liLen)

sqOddList = [x*x for x in range(1, 11) if x%2 == 1]
print(sqOddList)