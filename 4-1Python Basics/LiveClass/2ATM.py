def atm():
    print("Welcome to the ATM!")
    pin = "1234"
    balance = 1000

    enteredPIN = input("Enter your 4 digit PIN or type 'exit' to quit: ")

    while (True):
        if (enteredPIN == pin):
            print("\n### Options:")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Change PIN")
            print("5. Exit\n")

            choice = int(input("Enter your option: "))

            if (choice == 1):
                print(f"Your balance: ${balance}")
            elif (choice == 2):
                amount = float(input("Enter the amount to withdraw: $"))

                if (amount > balance):
                    print("Insufficient balance!!!\n")
                else:
                    balance -= amount
                    print(f"${amount} has been withdrawn. Remaining balance: ${balance}\n")
            elif (choice == 3):
                amount = float(input("Enter the amount to deposit: $"))  
                balance += amount
                print(f"${amount} has been deposited. New balance: ${balance}\n")
            elif (choice == 4):
                newPIN = input("Enter your new 4 digit PIN:")
                if (len(newPIN) == 4 and newPIN.isdigit()):
                    pin = newPIN
                    enteredPIN = newPIN
                    print("PIN changed successfully!\n")
                else:
                    print("Invalid PIN format (-_-). PIN must be 4 digit number.\n")
            elif (choice == 5):
                print("Thanks for banking with us. \nHave a nice day!\n")
                break
        elif(enteredPIN.lower() == "exit"):
            print("Exit successfully. \nHave a nice day!\n")
            break
        else:
            print("Wrong PIN entered, please try again\n")
            enteredPIN = input("Enter your 4 digit PIN or type 'exit' to quit: ")


atm()