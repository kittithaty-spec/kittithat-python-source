""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Vehicle info:\nBrand:{self.rand}, model:{self.model}, year: {self.year}"
        
class car(Vehicle):
    def __int__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year, number_of_doors)
        self.number_of_doors = number_of_doors

    def get_info(self):
        f"Vehicle info:\nBrand:{self.brand}, model:{self.model}, year: {self.year}, number of door: {self.number_of_doors}"


vehicle = Vehicle("toyota", "yaris", "2025")
print(vehicle.get_info())

car = car("honda", "city", "2029", "5")
print(car.get_info())
