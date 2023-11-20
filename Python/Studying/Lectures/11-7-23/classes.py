class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoter = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def Read_odometer(self):
        print("This car has " + str(self.odomoter) + " miles on it.")

    def FillGasTank(self):
        print("This car has a full gas tank")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year) # Creates instance of Car 
        self.battery_size = 75
        

    def charge(self):
        print(f"This {self.model} is charging")

    def FillGasTank(self):
        print("This car Doesnt have a gas tank")

MyCar = Car('chevy','camaro',2021)
MyOtherCar = ElectricCar('tesla','model S',2021)

## The child class can still use stuff defined in the parent class
print(MyCar.get_descriptive_name())
print(MyOtherCar.get_descriptive_name())
# MyOtherCar.Read_odometer()

## The parent class canot use stuff defined in the child class
# MyCar.charge() 

print("\n\n")
MyCar.FillGasTank()
MyOtherCar.FillGasTank()
