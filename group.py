import random
customer = dict()
class BankAccount:
    def __init__(self, name, acc_num, bal, ir):
        self.name = name
        self.account = acc_num
        self.bal = bal
        self.ir = ir
    def deposit(self, acc: int, dep: int) -> int:
        self.bal += dep
        return self.bal
    def withdraw(self, acc: int, dep: int) -> int:
        if self.bal >= dep:
            self.bal -= dep
            return self.bal
        else:
            return "Insufficient funds, enter valid amount"
    def set_interest_rate(self, acc: int, ir: float) -> None:
        self.ir = ir
        return self.ir
    def calculate_expected_return(self, acc: int, years: int) -> float:
        return self.bal * (1+self.ir) ** years
    def print_info(self):
        print("Name: " + self.name)
        print("Account: " + str(self.account))
        print("Balance: " + str(self.bal))
        print("Interest Rate: " + str(self.ir))


def create_account(n: str, dep: int, ir: float) -> int:
    r = rand_num()
    customer[r] = BankAccount(n, r, dep, ir)
    return r
    # dictionaries dont allow duplciate keys, is replaced

def rand_num() -> int:
    return random.randint(10000000, 100000000)

def check_acc(acc): 
    if acc in customer:
        return True
    else:
        return False

def run_bank():
    choice = int(input("1. Create account \n2. Deposit \n3. Withdraw \n4. Set interest rate \n5. Calculate return \n6. Show account info \n7. Exit \nInput: "))
    if choice == 1:
        name = input("What is your full name: ")
        dep = int(input("What is your intial deposit: "))
        ir = 4.25
        # set by user?
        print("ACCOUNT SUCCESSFULLY CREATED")
        print("Account number: " + str(create_account(name, dep, ir)) + " Interest rate: " + str(ir))
    elif len(customer)==0:
        print ("Please create an account first.")
    else:
        if choice == 2:
            acc = int(input("What is you account number: "))
            if check_acc(acc):
                dep = int(input("How much do you want to deposit: "))
                if dep > 0:
                    print("New balance: " + str(customer[acc].deposit(acc, dep)))
                else:
                    print("Please try again and input a positive number.")
            else:
                print("Invalid account number, try again.")
        elif choice == 3:
            acc = int(input("What is you account number: "))
            if check_acc(acc):
                dep = int(input("How much do you want to withdraw: "))
                print("New balance: " + str(customer[acc].withdraw(acc, dep)))
            else:
                print("Invalid account number, try again.")
        elif choice == 4:
            # interest rate limits
            acc = int(input("What is you account number: "))
            if check_acc(acc):
                ir = float(input("Input new interest rate: "))
                print("New interest rate: " + str(customer[acc].set_interest_rate(acc, ir)))
            else: 
                print("Invalid account number, try again.")
        elif choice == 5:
            acc = int(input("What is you account number: "))
            if check_acc(acc):
                year = int(input("How many years do you want to calculate:"))
                if year >= 0:
                    print("Expected return: " + str(customer[acc].calculate_expected_return(acc, year)))
                else:
                    print("Input a valid year.")
            else: 
                print("Invalid account number, try again.")
        elif choice == 6:
            acc = int(input("What is you account number: "))
            if check_acc(acc):
                customer[acc].print_info()
            else: 
                print("Invalid account number, try again.")
        elif choice == 7:
            run = False
        else:
            print("Invalid input, try again.")
    print()
    

                    
run = True
print("Welcome to Student Bank!")
print()
while run:
    run_bank()



