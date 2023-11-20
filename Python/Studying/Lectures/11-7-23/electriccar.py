from classes import Car

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year) # Creates instance of Car 
        self.battery_size = 75
        

    def charge(self):
        print(f"This {self.model} is charging")

    def FillGasTank(self):
        print("This car Doesnt have a gas tank")
