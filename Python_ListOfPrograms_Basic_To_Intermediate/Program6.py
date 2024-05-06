# Multiplication Table

number = int(input("Enter a number"))
print(".........Multiplication Table.........")
print(f"{number} * 1 = {number}")
print(f"{number} * 2 = {number * 2}")
print(f"{number} * 3 = {number * 3}")
print(f"{number} * 4 = {number * 4}")
print(f"{number} * 5 = {number * 5}")
print(f"{number} * 6 = {number * 6}")
print(f"{number} * 7 = {number * 7}")
print(f"{number} * 8 = {number * 8}")
print(f"{number} * 9 = {number * 9}")
print(f"{number} * 10 = {number * 10}")

# Multiplication Table using For loop

n = int(input("Enter a number to find out the multiplication table"))
count = 10
for i in range(1, count + 1):
    print(f"{n} * {i} = {i * n}")
