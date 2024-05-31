runnigTotal = 0

while(True):
    curr = input("Enter a number or quit to exit: ")

    if (curr == "quit"):
        break
    else:
        curr = int(curr)
        runnigTotal += curr
        print("Running total: ", runnigTotal)
