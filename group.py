import random
customer = []
class BankAccount:
    def __init__(self, name, acc_num, bal, ir):
        self.name = name
        self.account = acc_num
        self.bal = bal
        self.ir = ir
    def create_account(self, n: str, dep: int, ir: float) -> None:
        customer.append(BankAccount(n, random.randint(10000000, 100000000), dep, ir))
    def deposit(self, acc: int, dep: int): -> int:
        for ba in customer:
            if ba.account == acc:
                ba.bal +=dep
                balance = ba.bal
                return balance
    def withdraw(self, acc: int, dep: int) -> int:
        for ba in customer:
            if ba.account == acc:
                if ba.bal >= dep:
                    ba.bal -= dep
                    balance = ba.bal
                    return balance
                else:
                    raise ValueError("Insufficient funds")
    def set_interest_rate(self, acc: int, ir: float) -> None:
        for ba in customer:
            if ba.account == acc:
                ba.ir = ir
                return
    def calculate_expected_return(self, acc: int, years: int) -> float:
        for ba in customer:
            if ba.account == acc:
                return ba.bal * (1 + ba.ir) ** years
        return 0.0
