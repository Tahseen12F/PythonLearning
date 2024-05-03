# TASK2_WEEK3
# Factorial of a number
# 5! = 5*4*3*2*1
num = int(input("Enter a number :"))
fact = 1
while num > 1:
    fact = fact * num
    num = num - 1
print(f"Factorial of a number : {fact}")

# Fibonacci Series
# 0 1 1 2 3 5 8 13........
step = int(input("Enter the number of steps for Fibonacci series :"))
a = 0
b = 1
print("Fibonacci series are :")
print(a)
print(b)
i = 3
while i <= step:
    c = a+b
    print(c)
    a = b
    b = c
    i = i+1





