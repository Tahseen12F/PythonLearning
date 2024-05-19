# Exceptions in Python
# Try and Except block
# try - try the code
# Except - Execute the except code whenever there is an error in a try block.
# Note : Only Try block is not accepted in program.
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print("Error :", error)

print("............................................................")
a = int(input("Enter the first num : \n"))
b = int(input("Enter the second num : \n"))

try:
    c = a / b  # ZeroDivisionError : Division by Zero
    print("Result is :", c)

except Exception as e:
    print(e)
    print("Div with 0, Please don't use second num as 0")
    print("This is an important message")
