# class Student:
#     name = "jakaria"
#     def __init__(self):
#         print(self)
#         print("Adding student in database...")

# s1 = Student()
# print(s1)








# class Student:
#     def __init__(self, fullname, age):
#         self.name = fullname
#         self.age = age
#         print("Adding student in database...")

# s1 = Student("Jakaria Ahmed", 25)
# print(s1.name, s1.age)

# s2 = Student("Mishal Ahmed", 24)
# print(s2.name, s2.age)










# class Student:
#     #default constructor
#     def __init_(self):
#         pass

#     #parameterized constructor
#     def __init__(self, fullname, age):
#         self.name = fullname
#         self.age = age
#         print("Adding student in database...")

# s1 = Student("Jakaria Ahmed", 25)
# print(s1.name, s1.age)








class Student:
    clg_name = "Bujunga College"

    def __init__(self, fullname, age):
        self.name = fullname
        self.age = age
        print("Adding student in database...")

    def Welcome(self):
        print("WElcome Student", self.name)

    def get_age(self):
        return self.age

s1 = Student("Jakaria Ahmed", 25)
print(s1.name, s1.age)

s2 = Student("Mishal Ahmed", 24)
print(s2.name, s2.age)


# print(s1.clg_name)
# print(Student.clg_name)


s1.Welcome()
s2.Welcome()


print(s1.get_age())

