# Program to find the Area of Triangle
base = float(input("Enter the base of a triangle (in cm) : \n"))
height = float(input("Enter the height of a triangle (in cm) : \n"))
Area = 0.5 * base * height
print("Area of a triangle is : ", Area, "cm")
print(".............................")


# Program to find the Area of Triangle using function
def area_of_triangle(base, height):
    return 0.5 * base * height


base = float(input("Enter the base of a triangle (in cm) : \n"))
height = float(input("Enter the height of a triangle (in cm) : \n"))
print("Area of a triangle is : ", area_of_triangle(base, height), "cm")
