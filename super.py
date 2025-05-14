class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stop!")


class ToyotaCar(Car):
    def __init__(self,name, type):
        self.name = name
        super().__init__(type)



car1 = ToyotaCar("corolla", "electric")
print(car1.type)

