try:
    a=int(input("Enter Number1:"))
    b=int(input("Enter Number2:"))
    print("Result:",a/b)
except Exception as msg:
    print(msg)