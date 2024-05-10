# Program for Calculator
class Calc:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


a = Calc()
result = a.add(3, 4)
print(result)
