# Swapping of Number
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(f" a value is {a} and b value is {b} before swapping")
temp = a
a = b
b = temp
print(f" a value is {a} and b value is {b} after swapping")


# Swapping of Number using Function
def swap_num(x, y):
    z = x
    x = y
    y = z
    return x, y


x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
print(f" x value is {x} and y value is {y} before swapping i.e. {x, y}")
print("Swapping of two number is :", swap_num(x, y))
