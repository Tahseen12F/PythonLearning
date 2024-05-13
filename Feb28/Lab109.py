# Multi Level Inheritance
class GrandFather:
    def home(self):
        print("3 BHK")


class Father(GrandFather):
    pass                    # Pass is a null operator


class Son(Father):
    def home2(self):
        print("My villa")


Ron = Son()
Ron.home()
Ron.home2()
mmd = Father()
mmd.home()
# mmd.home2()  - Not possible
gkd = GrandFather()
gkd.home()
# gkd.home2()  - Not possible
