# tpl = ("jakaria", "mishal", "rana", "imtiaz", "azad")

# r = len(tpl) - 1
# while r >=0:
#     print(tpl[r])
#     r = r-1

# tpl_list = list(tpl)
# tpl_list.reverse()
# tpl = tuple(tpl_list)
# print(tpl)

#-----------------------------------------
# tuple1 = (11,22)
# tuple2 = (88,99)

# tplList1 = list(tuple1)
# tplList2 = list(tuple2)

# tplList3 = tplList1
# tplList1 = tplList2
# tplList2 = tplList3

# tuple1 = tuple(tplList1)
# tuple2 = tuple(tplList2)


#OR YOU CAN DO THIS
# tuple1, tuple2 = tuple2, tuple1

# print(tuple1)
# print(tuple2)
#-------------------------------------------------
# tuplex = ("w",3,"r","e","s","o","u","r","c","e")

# length = len(tuplex) - 1
# print(tuplex[3])
# print(tuplex[length-3])
# --------------------------------------------
list = [2,5,4,8,12,15,19,20,17,23,45,50,4,10]
oddCount = 0
evenCount = 0
for i in list:
    if(i%2==0):
        evenCount += 1
    else:
        oddCount += 1

print("total even number is: ", evenCount)
print("total odd number is:", oddCount)

