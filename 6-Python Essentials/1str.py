food = "pizza".capitalize()
food2 = "PizzA"

print(food)

print(food[0], food[1], food[2])
print(type(food[0]))
#food[5] #Error

print(food[0:2])
print(food == food2)

s = "shah sayem"

s1 = s.lower()
s2 = s.upper()
print(s1, s2)

print(id(s))
s = s.title()
print(id(s))
print(s)

n = 5
print(id(n))

n = 10
print(id(n))


print(len(s))
print(s[-1]) #print(s[len(s)-1])
print(s[-1], s[-2], s[-3], s[-4])

country = "Bangladesh"
for curr in country:
    print(curr)

#country[2] = "N"  #Error

print(dir(s))



