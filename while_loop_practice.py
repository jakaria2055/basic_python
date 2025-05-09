
# #PRINT NUMBER FROM 1 TO 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1



# #PRINT 100 TO 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1




#pRINT THE MULTIPLICATION TABLE OF A NUMBER N
# n = 3
# i = 1
# while i <= 10:
#     print(n,"x", i, "=", n*i)
#     i += 1




#PRINT THE ELEMENT OF THE LIST [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 1
# n = 3
# while i <=100:
#     print(i)
#     i += n
#     n += 2




# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# i = 0
# while i < len(num):
#     print(num[i])
#     i += 1



#SEARCH FOR A NUMBER X IN THIS ARAAY
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 81
i = 1

while i < len(num):
    if(num[i] == x):
        print("Value found in index", i)
    i += 1