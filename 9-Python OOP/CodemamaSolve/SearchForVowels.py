s = input()

flag = False
for curr in s:
    if ((curr == "a" or curr == "e" or curr == "i" or curr == "o" or curr == "u") or (curr == "A" or curr == "E" or curr == "I" or curr == "O" or curr == "U")):
        print("The string contains a vowel.")
        flag = True
        break

if (not flag):
    print( "The string does not contain any vowel.")