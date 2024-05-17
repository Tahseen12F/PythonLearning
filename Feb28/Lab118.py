# Method Overloading : Same name of functions but with different parameters.
# Python doesn't support Method Overloading in Traditional sense

class MathUtil:
    def add(self, a, b=0, c=0):
        return a+b+c

    # def add(self, a, b):    -----> Not advisable
    #   pass

mathUtil = MathUtil()
oper = mathUtil.add(2)
oper = mathUtil.add(2, 4)
oper = mathUtil.add(2, 5, 9)

