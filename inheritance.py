
# class Car:
#     color = "Black"
#     @staticmethod
#     def start():
#         print("Car Started...")

#     @staticmethod
#     def stop():
#         print("Car Stop!")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("premio")
# car2 = ToyotaCar("corolla")

# print(car1.name)
# print(car2.name)
# print(car1.start())
# print(car2.stop())
# print(car1.color)








#MULTI LEVEL INHERITANCE
# class Car:
#     @staticmethod
#     def start():
#         print("Car Started...")

#     @staticmethod
#     def stop():
#         print("Car Stop!")

# class ToyotaCar(Car):
#     def __init__(self,band):
#         self.band = band


# class Premio(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Premio("patrol")
# car1.start()









#MULTIPLE INHERITANCE
# class A:
#     varA = ("Welcome to Class A")

# class B:
#     varB = ("Welcome to class B")

# class C(A, B):
#     varC = print("Welcome to class C")

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)
