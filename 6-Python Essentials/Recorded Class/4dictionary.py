numTwoWords = dict()

numTwoWords[1] = "One"
numTwoWords[2] = "Two"
numTwoWords[3] = "Three"
numTwoWords[4] = "Four"

print(type(numTwoWords), numTwoWords)

if (3 in numTwoWords):
    print("Yes,", numTwoWords[3])
else:
    print("Not available")

del numTwoWords[2]

for i in numTwoWords:
    print(i)

for key, val in numTwoWords.items():
    print(key, val)

numTwoWords2 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}

print(numTwoWords2.items())


fruits = {"a": "Aplle", "b": "Banana", "c": "Cherry"}
print(fruits["c"])
print(fruits.get('b'))

print(fruits.keys())
print(fruits.values())

# fruits.clear()

print(dir(numTwoWords))

