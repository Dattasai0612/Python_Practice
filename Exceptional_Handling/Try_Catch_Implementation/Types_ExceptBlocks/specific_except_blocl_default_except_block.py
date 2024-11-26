try:
    a=int(input("Enter Number1:"))
    b=int(input("Enter Number2:"))
    print("Result:",a/b)
except:
    print("Something Wrong")
# except ZeroDivisionError as msg:
#     print(msg)