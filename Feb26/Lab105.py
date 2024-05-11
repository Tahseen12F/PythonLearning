# Encapsulation example

class SecureClass:
    def submit(self):
        self.__password = "123"
        self.__userid = "admin"
        self.heading = "VWO Login"


chrome = SecureClass()
chrome.submit()
# here also chrome.__password and chrome.__userid not allowed. Since it's private

