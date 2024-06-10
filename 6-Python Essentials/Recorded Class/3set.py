s = set() #Empty set OR
st = {}

s.add(1)
s.add(2)
s.add(2)
s.add(3)

print(s)

st2 = {1, 3, 4, 5}
print(s | st2) #Union
print(s & st2) #Intersection

print(st2-s)

print(s ^ st2) #XOR

li = [1, 2, 3, 4, 5, 6, 7, 8]
newSet = set(li)

liF = list(newSet)

liN = list(set(li))

st2.intersection



