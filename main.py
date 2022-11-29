# class House():
#     """description and plan of future houses"""
#     def __init__(self, street, number, floor):
#         self.street = street
#         self.number = number
#         self.floor = floor
#
#     def check_build(self):
#         print("house number", self.number, "at", self.street, "street is already built")
#
# House1 = House("Moscow", 20, 9)
# House2 = House("Toktogul", 18, 12)
# print(House1.check_build())


# class Human():
#     """description of a human"""
#     def __init__(self, name, sex, height, age, weight):
#         self.name = name = input()
#         self.sex = sex
#         self.height = height
#         self.age = 0
#         self.weight = weight
#
#     def age_permit(self):
#         if self.age > 21:
#             print(self.name, "can enter the club")
#         else:
#             print(self.name, "can not enter")
#
#     def weight_class(self):
#         if self.weight >= 85:
#             print(self.name, "is heavyweight group:", self.weight, "kilograms")
#         elif 62 <= self.weight <= 79:
#             print(self.name, "is average weight group:", self.weight, "kilograms")
#         elif self.weight <= 61:
#             print(self.name, "is lightweight group:", self.weight, "kilograms")
#
#     # def check_input_age(self):
#     #     print(self.name, "age is", 2022 - year)
#
# Human1 = Human("", "male", 178, 38, 89)
# Human2 = Human("", "female", 169, 24, 59)
# Human3 = Human("", "female", 173, 30, 70)
#
#
# print(Human1.weight_class())
# print(Human2.weight_class())
# print(Human3.weight_class())
# print(Human3.check_input_age(2005))


class cars():
    def __init__(self, name, type, volume, horsepower, cost, age, weight):
        self.name = name
        self.type = type
        self.volume = volume
        self.horsepower = horsepower
        self.cost = cost
        self.age = age
        self.weight = weight

    def tax(self):
        if self.age <= 5 or self.volume <= 2.0:
            print(f"the tax for {self.name} is $100 per year")
        elif self.age > 5 or self.volume > 2.0:
            print(f"the tax for {self.name} is $300 per year")


car1 = cars("BMW M340i", "sedan", 3.0, 380, 5500, 1, 1800)
car2 = cars("Genesis G90", "sedan", 2.5, 280, 80000, 2, 2200)
car3 = cars("Mazda MX-5", "coupe", 2.0, 210, 31000, 4, 1150)

print(car3.tax(), car1.tax())
