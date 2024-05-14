# Hybrid Inheritance
class A:
    def MethodA(self):
        return "Method A"


class B(A):
    def MethodB(self):
        return "Method B"


class C(A):
    def MethodC(self):
        return "Method C"


class D(B, C):
    def MethodD(self):
        return "Method D"


d = D()
print(d.MethodA())
print(d.MethodB())