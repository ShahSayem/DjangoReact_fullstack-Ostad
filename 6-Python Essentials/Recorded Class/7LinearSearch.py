li = [1, 3, 6, 10, 100, 14, 5, 9]

# idx = li.index(5)
# isFound = 15 in li


key = 4
isFound = False

for num in li:
    if (num == key):
        print(key, "Found")
        isFound = True
        break
    
if (not isFound):
    print("Not Found!!!")