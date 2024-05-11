# Program sample (Use of Class in automation)

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def LoginConfirm(self):
        if self.password == "Pass123":
            print("You are allowed to login")
        else:
            print("Invalid")


tash = VWOLoginPage("tas123@mail.com", "123")
tash.LoginConfirm()
shau = VWOLoginPage("sha123@mail.com", "Pass123")
shau.LoginConfirm()

""" Note - Using encapsulation in Python helps users to not access the state values for all the variables of an 
individual object. 
Using Encapsulation in Python we can hide both data functions and data members or methods that are associated with an instance of a class."""
# Note - Here in the above code we can easily access password of any user. This will breach security.
# So, to avoid this , we need the concept of Encapsulation.
