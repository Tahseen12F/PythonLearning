class Student:
    name = None
    Id = None
    age = None
    address = None
    course = None
    payment = None

    def addStudent(self):
        print("......New student added......")
        print("student name : ", self.name)
        print("studentId :", self.Id)
        print("student age :", self.age)
        print("student address :", self.address)

    def Course(self):
        print("......Course Name......")
        print("Course name : ", self.course)

    def Payment(self):
        print("......Total Payment......")
        print("Course name : ", self.payment)


student_name = input("Enter student name")
student_Id = input("Enter student Id")
student_age = int(input("Enter student age"))
student_address = input("Enter student address")
student_course = input("Enter student course name")
student_payment = float(input("Enter student course payment"))

student_obj = Student()
student_obj.name = student_name
student_obj.Id = student_Id
student_obj.age = student_age
student_obj.address = student_address
student_obj.course = student_course
student_obj.payment = student_payment

student_obj.addStudent()
student_obj.Course()
student_obj.Payment()
