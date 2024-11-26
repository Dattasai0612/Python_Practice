try:
    print("Statement 1")
    print(10/0)
    print("Statement 2")
    print(10/0)
    print("Statement 3")
except:
    # print(10/0)
    print("Statement 4")
print("Statement 5")

# 1,2,3,5 -> comment Line-4
# 1,4,5 -> comment Line-8, add print(10/0) Line-3
