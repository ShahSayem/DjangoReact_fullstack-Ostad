runnigTotal = 0

while(True):
    curr = input("Enter a number or quit to exit: ")

    if (curr == "quit"):
        break
    else:
        try:
            curr = float(curr)
            runnigTotal += curr
            print("Running total: ", runnigTotal)
        except:
            print("Your inpur is in incorrect format(-_-) \nTry again!!!")
