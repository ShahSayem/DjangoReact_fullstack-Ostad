items = [1, 2, 3, "abc", 10.5]
print(type(items))

print(items[1])
print(items[-1])

print(len(items))

x = "abc"
print(x in items)
print("xyz" in items)
print(3 in items)

items[2] = 7 
for curr in items:
    print(curr)


city = "Sylhet"  
li = list(city)  
li[0] = "s"

print(li)


myList = ["s", "y", "l", "h", "e", "t"]
myList[0] = "0"

str = "".join(myList) #join by "", we can also use: "+", "-"
print(str)
