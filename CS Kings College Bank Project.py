import random

def bank():
    account = {}
    balance = 0
    deposit_time = 0
    withdraw_time = 0
    process = False
    intrest_rate = 0
    time = 0
    possible_earnings = 0
    deposit_time = 0
    withdraw_time = 0
    amount_deposit = 0
    amount_withdraw = 0

    while True:
        create = input("Do you want to create a Bank Account: ")
        if create == "yes":
            account_name = input("What Is Your Name: ")
            account_number = [str(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))]
            for i in range(7):
                account_number.append(random.choice(["2", "3", "4", "5", "6", "7", "8", "9"]))
            account_number = ''.join(account_number)
            print("Generated account number:", account_number)
            balance = float(input("Insert Balance: "))
            if balance < 0:
                print("Be serious")
                balance = float(input("Insert Balance: "))
            
            account = (f"Account Name: {account_name}\n"
                  f"Account Number: {account_number}\n"
                  f"Balance: {balance}$\n")
            print("\nAccount created successfully! ")
            print(account)
            break
        elif create.lower == "no":
            print("so why Bother trying the program")
            break
        else:
            print("Answer not accepted, please try again")
        
    while True:
        selection = input("Choose which action to follow:\n"
                          "1. Deposit\n"
                          "2. Withdraw\n"
                          "3. Set interest rate\n"
                          "4. Calculate Investment\n"
                          "5. Show account info\n"
                          "6. Exit\n"
                          "Enter your choice: ")

        if selection == "1" or selection.lower() == "deposit":
            deposit_time += 1
            amount_deposit = float(input("How much do you want to deposit? "))
            if amount_deposit > 0:
                balance += amount_deposit
                total_deposit = amount_deposit
                print(f"New balance: {balance}$\n")
            else:
                print("You can't Deposit a negative amount of money")
            
        
        elif selection == "2" or selection.lower() == "withdraw":
            withdraw_time += 1
            amount_withdraw = float(input("How much do you want to withdraw "))
            if amount_withdraw > balance or amount_withdraw < 0:
                print("Amount inserted is superior to your Balance")
            elif amount_withdraw <= balance:
                balance -= amount_withdraw
            print(f"New Balance: {balance}$\n")
        
        elif selection == "3" or selection.lower() == "Set interest rate":
            intrest_rate = float(random.choice(["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9"]))
            print(f"Intrest Rate set at:  {intrest_rate}\n")
            account = (f"Account Name: {account_name}\n"
                  f"Account Number: {account_number}\n"
                  f"Balance: {balance}$\n"
                  f"Intrest Rate: {intrest_rate}\n")
            process = True
        
        elif selection == "4" or selection.lower() == "Calculate investment":
            if process == True:
                time = float(input(f"Your intrest rate is {intrest_rate}, how many years would you like to invest? "))
                possible_earnings = balance*(intrest_rate)**time
                print(f"These are your possible earnings: {possible_earnings}$\n")
            elif process == False:
                print("You first have to set an intrest rate")
        
        elif selection == "5" or selection.lower() == "Show account info":
            print(f"\nBelow is the account information of {account_name}\n"
                  f"Account Number: {account_number}\n"
                  f"Balance: {balance}$\n "
                  f"Intrest Rate: {intrest_rate}\n"
                  f"Investing {time} years\n"
                  f"Possible Return Investment: {possible_earnings}$\n")
            transaction_log = input("\nDo you want to see your Transaction History?")
            if transaction_log == "yes":
                print(f"\nThe amount of times you deposited money is {deposit_time} and you deposited {amount_deposit}$\n "
                      f"The amount of times you withdrew money is {withdraw_time} and you withdrew {amount_withdraw}$\n")
            elif transaction_log == "no":
                print("Answer not accepted, try again")
            else:
                print("Answer not accepted, try again")


        elif selection == "6" or selection.lower() == "Exit":
            print("\nThanks for using our Bank!\n")
            break
        
        else:
            print("Please insert one of the options")

bank()