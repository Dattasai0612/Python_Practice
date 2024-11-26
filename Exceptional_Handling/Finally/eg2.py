import os
try:
    print(10/0)
    print("Try Block")
    # os._exit(0)
except:
    print("Except Block")
    # os._exit(0)
finally:
    print("Finally Block")