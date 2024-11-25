class Test:
    x=10    #public
    _y=20   #protected
    __z=30  #private

    def __init__(self):
        print("Within Class")
        print(self.x)
        print(self._y)
        print(self.__z)

t=Test()
print("Outside Class")
print(t.x)
print(t._y)
# print(t.__z)    #Attritubr Erroe