# Task1_Week3
# Calculate the sum of 2 numbers using function.
def sum_num(a, b):
    return a + b


result = sum_num(2, 4)
print(result)


# Factorial using function
def fact(n):
    factorial = 1
    while n > 1:
        factorial = factorial * n
        n = n - 1
    return factorial


num = int(input("enter the num"))
print("factorial of num is :",fact(num))

