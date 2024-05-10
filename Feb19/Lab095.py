class Person:
    # Attributes -> Data members
    name = None
    age = None
    id = None
    phn_num = None

    # Behaviour -> Methods
    def talk(self):
        print("I can talk")

    def sleep(self):
        print("I can sleep")


# Object creations -> className()
abc = Person()
xyz = Person()
xyz.name = "Tashu"
print(xyz.name)
abc.talk()

