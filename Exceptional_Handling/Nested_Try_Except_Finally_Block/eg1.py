try:
    print(10/0)
    print("Outer Try")
    try:
        print(10/0)
        print("Inner Try")
    except ValueError:
        print("Inner Except")
    finally:
        print("Inner Finally")
except:
    print("Outer Except")
finally:
    print("Finally Except")