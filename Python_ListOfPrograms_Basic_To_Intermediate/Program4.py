# Program to check a number whether +ve, -ve or 0
num = int(input("Enter a number : "))
if num == 0:
    print("The given number is :", num)
elif num > 0:
    print("The given number is positive :", num, "which is positive")
else:
    print("The given number is :", num, "which is negative")


# Program to check a number whether +ve, -ve or 0 using function
def num_identity(number):
    if number == 0:
        return "zero"
    elif number > 0:
        return "positive"
    else:
        return "negative"


number = int(input("Enter a number"))
print("The given number is ", num_identity(number))
