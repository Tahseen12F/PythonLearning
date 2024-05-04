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
print("factorial of num is :", fact(num))


# Reverse of String using Function
def reverse_number(name):
    str = input("Enter the name")
    original_str = str
    rev_str = " "
    for c in str:
        rev_str = c + rev_str
    return rev_str


print("Reverse of string", reverse_number(str))


# Palindrome

def reverse_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


original_str = input("Enter the String\n")
original_str = original_str.lower()
rev_str = reverse_string(original_str)
print(rev_str)

# Palindrome - str = rev_str -> p
if original_str == rev_str:
    print("Palindrome")
else:
    print("Not a Palindrome")


