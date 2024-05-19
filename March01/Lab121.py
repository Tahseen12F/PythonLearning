# try, except and finally block
# Multiple Exception
try:
    a = int(input("Enter the first num : \n"))
    b = int(input("Enter the second num : \n"))
    c = a / b  # ZeroDivisionError : Division by Zero
except ValueError as ve:
    print(ve)
except ZeroDivisionError as ze:
    print("Not allowed",ze)
else:
    print(f"Result is :",{c})
finally:
    print("I will be executed anyhow!!")