# class Student:
#     def __init__(self, name, ban, eng, math):
#         self.name = name
#         self.ban = ban
#         self.eng = eng
#         self.math = math

#     def avg(self):
#         sum = self.ban + self.eng + self.math
#         avg = sum / 3
#         return avg
# s1 = Student("Rana", 50, 60, 70)
# s2 = Student("Emtiaz", 60, 70, 80)
# s3 = Student("Mishal", 70, 80, 90)

# print(s1.avg())
# print(s2.avg())
# print(s3.avg())





class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your average marks is: ", sum/3)

s1 = Student("Mishal", [70, 80, 90])
s1.avg()