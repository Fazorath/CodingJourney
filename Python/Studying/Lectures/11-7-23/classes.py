class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoter = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odomoter) + " miles on it.")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year) # Creates instance of Car 
        

    def charge(self):
        print(f"This {self.model} is charging")

MyCar = Car('chevy','camaro',2021)
MyOtherCar = ElectricCar('tesla','model S',2021)

print(MyCar.get_descriptive_name())
print(MyOtherCar.get_descriptive_name())
MyOtherCar.read_odometer()
