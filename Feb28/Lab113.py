# Multiple Inheritance
# Father, Mother -> Son
class Father:
    def father_money(self):
        return 5

    def Home(self):
        return "This is a Father's home"


class Mother:
    def mother_money(self):
        return 2

    def Home(self):
        return "This is a Mother's home"


class Son(Father, Mother):
    pass


son = Son()
print(son.father_money())
print(son.mother_money())
print(Son().Home())
