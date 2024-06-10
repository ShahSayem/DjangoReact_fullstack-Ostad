# Dictionary
li = [(1, "One"), (2, "Two"), (3, "Three")]
dt = {k:v for k, v in li}
print(dt)

dt2 = {v:k for k, v in li}
print(dt2)

# Set
s = "abcdefabcdef"
uniqueLetters = {c for c in s}
print(type(uniqueLetters), uniqueLetters)



############
colorsChoice = [("Sayem", "Blue"), ("Hasan", "Red"), ("Rafi", "Green"), ("Nadim", "Blue")]
print(colorsChoice)

colorsDt = {name:color for name, color in colorsChoice}
print(colorsDt)

colorsSet = {clr for clr in colorsDt.values()}
print(colorsSet)
