# ATM Simulation

correct_pin = "1234"
balance = 10000
transactions = []

print("========== WELCOME TO ATM ==========")

# PIN Verification
attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Wrong PIN.")
        print("Attempts remaining:", attempts)

# If PIN is wrong 3 times
if attempts == 0:
    print("Your account is locked.")

else:

    # ATM Menu
    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # 1. Check Balance
        if choice == "1":

            print("\nYour current balance is:", balance)

        # 2. Deposit
        elif choice == "2":

            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance = balance + amount
                transactions.append(f"Deposited: ₹{amount}")

                print("Deposit successful!")
                print("Updated balance:", balance)

            else:
                print("Invalid amount.")

        # 3. Withdraw
        elif choice == "3":

            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount.")

            elif amount > balance:
                print("Insufficient balance.")

            elif amount > 20000:
                print("Maximum withdrawal limit is ₹20,000.")

            else:
                balance = balance - amount
                transactions.append(f"Withdrawn: ₹{amount}")

                print("Please collect your cash.")
                print("Remaining balance:", balance)

        # 4. Transaction History
        elif choice == "4":

            print("\n========== TRANSACTION HISTORY ==========")

            if len(transactions) == 0:
                print("No transactions yet.")

            else:
                for transaction in transactions:
                    print(transaction)

        # 5. Exit
        elif choice == "5":

            print("\nThank you for using the ATM!")
            break

        # Invalid option
        else:
            print("Invalid choice. Please select 1-5.")

