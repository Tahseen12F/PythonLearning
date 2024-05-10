# Use of self Variable

class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

    def start_engine(self):
        print("Starting engine")

    def drive(self):
        print("drive")

    def who_is_driving(self):
        print("I'm driving ->" + self.name)


# Object Creation
tesla_obj_car = Car()
lambo_obj_car = Car()

tesla_obj_car.name = "Tesla"
lambo_obj_car.name = "Lambo"

tesla_obj_car.who_is_driving()
lambo_obj_car.who_is_driving()