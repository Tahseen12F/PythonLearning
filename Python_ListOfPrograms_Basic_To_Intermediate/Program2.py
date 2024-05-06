# Add two number

a = int(input("Enter first Number"))
b = int(input("Enter second Number"))
sum_of_num = a + b
print("Sum of two number is: ", sum_of_num)


# Add two number using Function

def add_num(a, b):
    return a + b


a = int(input("enter 1st num"))
b = int(input("enter 2nd num"))
print("Sum of 2 num :", add_num(a, b))
