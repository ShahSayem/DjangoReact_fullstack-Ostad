marks = 80
result = ""

if (marks < 33):
    result = "Failed"
elif (marks >= 80):
    result = "Passed with A+"
else:
    result = "Passed"

print(result)


# letter = input("Enter a letter:")
letter = "g"

print(letter, "is a ")
match letter:
    case "a": print("vowel alphabet")
    case "e": print("vowel alphabet")
    case "i": print("vowel alphabet")
    case "o": print("vowel alphabet")
    case "u": print("vowel alphabet")
    case _: print("consonent alphabet")


print("While loop:")
i = 1
while(i <= 5):
    print(i)
    i += 1


words = ["one", "two", "three"]

for curr in words:
    print(curr)


def myFunc():
    print("myFunc called")