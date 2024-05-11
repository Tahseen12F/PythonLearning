# Bank Example using Access specifiers

class Bank:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def deposit(self, amount):
        self.balance += amount

    def _withdraw(self, amount):  # Protected
        self.balance -= amount

    def __show_balance(self):  # Private
        print("your balance", self.balance)

    def if_u_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")

    def do_withdrw_by_bankmanager(self, amount):
        self._withdraw(amount=amount)


jp_chase = Bank()
jp_chase.deposit(1000)
jp_chase.do_withdrw_by_bankmanager(499)
jp_chase.if_u_are_auth(True)
