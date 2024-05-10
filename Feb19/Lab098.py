# Multiple Parameters

class Mult_param:
    name = None

    def print_info(self, firstname, lastname, age):
        print("Your name is", firstname, lastname, age)


obj_ref = Mult_param()
obj_ref.print_info("Tahseen","Fatma",25)
