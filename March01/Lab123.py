# Custom Exception
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


balance = 1000
Withdraw_amt = int(input("Enter the amount you want to withdraw :"))

if Withdraw_amt > balance:
    raise MyCustomException("Balance is low!")
else:
    print("Total amt left : ", balance - Withdraw_amt )