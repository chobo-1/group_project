import random
customer = dict()
class BankAccount:
    def __init__(self, name, acc_num, bal, ir):
        self.name = name
        self.account = acc_num
        self.bal = bal
        self.ir = ir
    def deposit(self, acc: int, dep: int): -> int:
    for ba in customer.keys():
        if ba == acc:
            customer[ba].bal +=dep
            balance = customer[ba].bal
            return balance
    def withdraw(self, acc: int, dep: int) -> int:
        for ba in customer.keys():
            if ba == acc:
                if customer[ba].bal >= dep:
                    customer[ba].bal -= dep
                    balance = customer[ba].bal
                    return balance
                else:
                    raise ValueError("Insufficient funds")
    def set_interest_rate(self, acc: int, ir: float) -> None:
        for ba in customer.keys():
            if ba == acc:
                customer[ba].ir = ir
                return
    def calculate_expected_return(self, acc: int, years: int) -> float:
        for ba in customer:
            if ba.keys == acc:
                return ba.bal * (1 + ba.ir) ** years
        return 0.0

def create_account(n: str, dep: int, ir: float) -> None:
    r = rand_num()
    customer[r] = BankAccount(n, r, dep, ir)
    # dictionaries dont allow duplciate keys, is replaced

def rand_num() -> int:
    return random.randint(10000000, 100000000):

