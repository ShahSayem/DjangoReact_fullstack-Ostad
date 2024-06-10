try:
    fr = open("myFile2.txt", "r")

    content = fr.read()
    print(content)

    fr.close()
except:
    print("File not found!!!")

print("Program closed successfully")



while(True):
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))

    if (n1 == 0 and n2 == 0):
        break

    try:
        print("Division result: ", n1/n2)
    except ZeroDivisionError:
        print("Error,\n0 can not be a divisor!!!")
    else:
        print("No Exception")

print("Program closed successfully")