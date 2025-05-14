# class Bank:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Bank("12345", "abcde")

# print(acc1.acc_no)
# # print(acc1.__acc_pass)   #this is incorrect
# print(acc1.reset_pass())  







class Person:
    __name = "jakaria"

    def __hello(self):
        print("Hello Person!")

    def welcome(self):
        self.__hello()

p1 = Person()
# print(p1.__name)
# print(p1.__hello())  #both of them are private, not print

print(p1.welcome())


