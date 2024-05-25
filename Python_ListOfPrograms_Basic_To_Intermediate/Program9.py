# Quadratic Equation
# Formula For Quadratic equation (ax2 + bx + c = 0) ; Discriminant = b*b - 4*a*c
# If the discriminant value is positive, the quadratic equation has two real and distinct solutions.
# If the discriminant value is zero, the quadratic equation has only one solution or two real and equal solutions.
# If the discriminant value is negative, the quadratic equation has no real solutions.

a = int(input("Enter a value of a : \n"))
b = int(input("Enter a value of b : \n"))
c = int(input("Enter a value of c : \n"))
if a == 0:
    print("Invalid Quadrilateral ")
else:
    discriminant = b*b-4*a*c
    print("Discriminant of equation is :", discriminant)
    if discriminant > 0:
        print("The quadratic equation has two real and distinct solutions")
    elif discriminant == 0:
        print("The quadratic equation has only one solution or two real and equal solutions")
    else:
        print("The quadratic equation has no real solutions")

