
# with open("prctc.txt","w") as f:
#     f.write("I am jakaria.\n I am learning python.")
#     f.write("Then i will learn js.\n Then move into express.")


# with open("prctc.txt","r") as f:
#     data = f.read()

# new_data = data.replace("express", "nextjs")
# print(new_data)





#FIND A WORD IN FILE
# def check_for_word():
#     word = "learn"
#     with open("prctc.txt", "r") as f:
#         data = f.read()
#     if(data.find(word) != -1):
#         print("WOrd found.")
#     else:
#         print("Not found")

# check_for_word()




# def check_for_line():
#     word = "express"
#     data = True
#     line_no = 1
#     with open("prctc.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
    
#     return -1
# check_for_line()





# with open("prctc.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i]==","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]





# with open("prctc.txt", "r") as f:
#     data = f.read()
#     print(data)

#     nums = data.split()
#     print(nums)





#TOTAL NUMBER OF EVEN NUMBER
count = 0
with open("prctc.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)
