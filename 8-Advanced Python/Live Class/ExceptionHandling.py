try:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))

    print(n1/n2) 
except ZeroDivisionError:
    print("Error!!! Can not divide by 0. Please enter a non-zero number in 2nd number")
except ValueError:
    print("Enter number only!")
except TypeError:
    print("Error!!! Please contact the developer!")
