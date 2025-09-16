""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year 
    

def get_info(self):
    return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(vehicle):
    def __init__(self, brand, model, year, number_of_door):
        super().__init__(brand, model ,year)
        self.number_of_door = number_of_door

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Doors: {self.number_of_door}"
    
    myCar = Car("Toyota", "Prius", 2022, 5)
    print(myCar.get_info())