# Hierarchical Inheritance
class Father:
    def Home(self):
        return "This is a Father's home"


class Son1(Father):
    pass


class Son2(Father):
    def Home(self):
        return "This is a son2 home"


Jack = Son1()
Mike = Son2()
print(Jack.Home())
print(Mike.Home())
