tpl = (1, 2, 3)

print(type(tpl), tpl)
print(tpl[-1])

for i in tpl:
    print(i)

# tpl[0] = 10 //Immutable -> Error!

tpl2 = 2, 4, 6, 8 #pack

tpl3 = tuple() #Empty tuple

# print(dir(tuple))

a, b, c = tpl #unpack
print(a, b, c)