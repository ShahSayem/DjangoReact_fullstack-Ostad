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

            choice = input("Enter your option: ")

            if (choice == "1"):
                print(f"Your balance: ${balance}")

            elif (choice == "2"):
                amount = input("Enter the amount to withdraw: $")

                try:
                    amount = float(amount)

                    if (amount > balance):
                        print("Insufficient balance!!!\n")
                    else:
                        balance -= amount
                        print(f"${amount} has been withdrawn. Remaining balance: ${balance}\n")
                except ValueError:
                    print("Invalid amount format (-_-). Amount must be in numeric format.\n")

            elif (choice == "3"):
                amount = input("Enter the amount to deposit: $")

                try:
                    amount = float(amount)
                    balance += amount
                    print(f"${amount} has been deposited. New balance: ${balance}\n")
                except ValueError:
                    print("Invalid amount format (-_-). Amount must be in numeric format.\n")

            elif (choice == "4"):
                newPIN = input("Enter your new 4 digit PIN:")
                if (len(newPIN) == 4 and newPIN.isdigit()):
                    pin = enteredPIN = newPIN
                    print("PIN changed successfully!\n")
                else:
                    print("Invalid PIN format (-_-). PIN must be 4 digit number.\n")
                    
            elif (choice == "5"):
                print("Thanks for banking with us. \nHave a nice day!\n")
                break
            else:
                print("Invalid opotion format (-_-). Option must be a single digit number from 1 to 5.\n")

        elif(enteredPIN.lower() == "exit"):
            print("Exit successfully. \nHave a nice day!\n")
            break
        else:
            print("Wrong PIN entered, please try again\n")
            enteredPIN = input("Enter your 4 digit PIN or type 'exit' to quit: ")


atm()