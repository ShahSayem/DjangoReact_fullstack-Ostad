while(True):
    s = input()

    if (s == "quit"):
        print("Quit")
        break
    elif (s == "skip"):
        print("Skipped!!!")
        continue

    print(s.upper())