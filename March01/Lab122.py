class AB:
    def f1(self):
        try:
            a = int(input("Enter a number : \n"))
        except Exception as e:
            print("Enter only Integer in the value of a. Else you will get an error msg")
        else:
            print(a)
        finally:
            print("Anyhow it will be printed")


ab = AB()
ab.f1()
