try:
    a=int(input("Enter Number1:"))
    b=int(input("Enter Number2:"))
    print("Result",a/b)
except ZeroDivisionError as msg:
    print(msg)
except ValueError as msg:
    print(msg)