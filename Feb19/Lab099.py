class Car:
    color = None
    model = None

    def car_details(self):
        print("Your car detail is", self.color, self.model)


car_color = input("Enter your car color")
car_model = input("Enter your car model")

car_obj = Car()
car_obj.color = car_color
car_obj.model = car_model

car_obj.car_details()