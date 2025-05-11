
# def calcSum(n):
#     if(n==0):
#         return 0
#     return calcSum(n-1) + n

# print(calcSum(10))






def printList(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    printList(list, idx+1)

fruits = ["apple", "banana", "cucmber", "dove", "egg", "fefe"]
printList(fruits)

