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
        ir = self.ir/100
        return self.bal * (1+ir) ** years
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
    while True:
        r = random.randint(10000000, 99999999)
        if r not in customer:
            return r

def check_acc(acc): 
    if acc in customer:
        return True
    else:
        return False
    
def transact(acc1, acc2, amt):
    result = customer[acc1].withdraw(acc1, amt)
    if isinstance(result, int):
        customer[acc2].deposit(acc2, amt)
        print("Account: " + str(acc1) + " has sent Account: " + str(acc2) + " $" + str(amt))
        print("Account: " + str(acc1) + " New balance: " + str(customer[acc1].bal))
        print("Account: " + str(acc2) + " New balance: " + str(customer[acc2].bal))
    else:
        print(result)

def run_bank():
    c = input("1. Create account \n2. Deposit \n3. Withdraw \n4. Show interest rate \n5. Calculate return \n6. Show account info \n7. Transact \n8. Exit \nInput: ")
    print()
    if c.isdigit():
        choice = int(c)
        if choice == 1:
            name = input("What is your full name: ")
            d = input("What is your intial deposit: ")
            if d.isdigit():
                dep = int(d)
                if dep > 0:
                    ir = 3.5
                    # set by user?
                    print("ACCOUNT SUCCESSFULLY CREATED")
                    print("Account number: " + str(create_account(name, dep, ir)) + " Interest rate: " + str(ir))
                else:
                    print("Please try again and input a positive number.")
            else:
                print("Invalid input, try again.")
        elif len(customer)==0:
            print ("Please create an account first.")
        else:
            if choice == 2:
                acc = int(input("What is your account number: "))
                if check_acc(acc):
                    d = input("How much do you want to deposit: ")
                    if d.isdigit():
                        dep = int(d)
                        if dep > 0:
                            print("New balance: " + str(customer[acc].deposit(acc, dep)))
                        else:
                            print("Please try again and input a positive number.")
                    else:
                        print("Invalid input, try again.")
                else:
                    print("Invalid account number, try again.")
            elif choice == 3:
                acc = int(input("What is your account number: "))
                if check_acc(acc):
                    d = input("How much do you want to withdraw: ")
                    if d.isdigit():
                        dep = int(d)
                        print("New balance: " + str(customer[acc].withdraw(acc, dep)))
                    else:
                        print("Invalid input, try again.")
                else:
                    print("Invalid account number, try again.")
            elif choice == 4:
                # interest rate limits
                acc = int(input("What is your account number: "))
                if check_acc(acc):
                    # ir = float(input("Input new interest rate: "))
                    # print("Interest rate: " + str(customer[acc].set_interest_rate(acc, ir)))
                    print("Interest rate: " + str(customer[acc].ir))
                else: 
                    print("Invalid account number, try again.")
            elif choice == 5:
                acc = int(input("What is your account number: "))
                if check_acc(acc):
                    year = int(input("How many years do you want to calculate:"))
                    if year >= 0:
                        print("Expected return: " + str(customer[acc].calculate_expected_return(acc, year)))
                    else:
                        print("Input a valid year.")
                else: 
                    print("Invalid account number, try again.")
            elif choice == 6:
                acc = int(input("What is your account number: "))
                if check_acc(acc):
                    customer[acc].print_info()
                else: 
                    print("Invalid account number, try again.")
            elif choice == 7:
                acc1 = int(input("What is your account number: "))
                acc2 = int(input("What account do you want to send to: "))
                if check_acc(acc1) and check_acc(acc2):
                    amt = int(input("How much do you want to send: "))
                    transact(acc1, acc2, amt)
                else:
                    print("Invalid input, try again.")
            elif choice == 8:
                print("Bank app has been closed")
                return False
            else:
                print("Invalid input, try again.")
    else:
        print("Invalid input, try again.")
    print()
    return True
    
            

print("Welcome to Student Bank!")
print()
run = True
while run:
    run = run_bank()




