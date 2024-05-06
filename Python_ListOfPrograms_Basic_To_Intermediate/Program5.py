# Program to find Largest among 3 numbers
a = int(input("Enter 1st num : "))
b = int(input("Enter 2nd num : "))
c = int(input("Enter 3rd num : "))
if a > b and a > c:
    print(f"{a} is the greatest among all")
elif b > a and b > c:
    print(f"{b} is the greatest among all")
else:
    print(f"{c} is the greatest among all")
