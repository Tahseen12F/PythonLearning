# TASK1_WEEK3
# Program that determines whether a given year is a leap year
year = int(input("Enter a year"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("This year is a leap year")
else:
    print("This is not a leap year")

# Program to classifies a triangle based on its sides (Equilateral, Isosceles, Scalene)
a = int(input("Enter side a : "))
b = int(input("Enter side b : "))
c = int(input("Enter side c : "))
if a == b and a == c and b == c:
    print("All sides are Equal, This is Equilateral Triangle")
elif (a == b and b == c and a != c) or (a !=b and b==c and a ==c) or (a ==b and b !=c and a==c):
    print("2 sides are Equal, This is Isosceles Triangle")
else:
    print("All sides are not Equal, This is Scalene Triangle")




