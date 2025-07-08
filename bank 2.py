import random

def bank():
    account = {}
    balance = 0
    while True:
        selection = input("Choose which action to follow:\n"
                          "1. Create account\n"
                          "2. Deposit\n"
                          "3. Withdraw\n"
                          "4. Set interest rate\n"
                          "5. Calculate Investment\n"
                          "6. Show account info\n"
                          "7. Exit\n"
                          "Enter your choice: ")

        if selection == "1" or selection.lower() == "create account":
            account_name = input("What Is Your Name: ")
            account_number = [str(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))]
            for i in range(7):
                account_number.append(random.choice(["2", "3", "4", "5", "6", "7", "8", "9"]))
            account_number = ''.join(account_number)
            print("Generated account number:", account_number)
            balance = float(input("Insert Balance: "))
            intrest_rate = random.choice(["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9"])
            account = {"Name": account_name,
                       "Account Number": account_number,
                       "Balance": balance,
                       "Intrest Rate": intrest_rate}
            print("\nAccount created successfully!")
            print(account)

        elif selection == "2" or selection.lower() == "deposit":
            amount_deposit = float(input("How much do you want to deposit? "))
            balance += amount_deposit
            print(f"New balance: {balance}")
        
        elif selection == "3" or selection.lower() == "withdraw":
            amount_withdraw = float(input("How much do you want to withdraw "))
            balance -= amount_withdraw
            print(f"New Balance: {balance}")


bank()
