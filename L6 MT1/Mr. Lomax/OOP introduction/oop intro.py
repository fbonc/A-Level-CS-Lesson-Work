class Car:
    def __init__(self, m):
        self._model = m
        self._fuel = 0
        self._distance = 0

    def __str__(self):
        return f"This {self._model} has {self._fuel} gallons of fuel, and has driven {self._distance}km"
    
    def fuel(self):
        self._fuel += 1
        print(f"Your {self._model} has {self._fuel} gallons of fuel")
    
    def drive(self):
        if self._fuel == 0:
            print("Not enough fuel to drive")
        else:
            self._fuel -= 1
            self._distance += 50
            print("You drove 50km")
            print(f"You have {self._fuel} gallons left of fuel")
    
    def showDistanceDriven(self):
        print(f"You have driven {self._distance}km")


car = Car("Aventador")


car.fuel()
car.drive()
# car.showDistanceDriven()
print(car)



# while True:
#     choice = input("\n1) Fuel\n2) Drive\n3) Show distance driven\n4) Exit\n")
#     if choice == "1":
#         car.fuel()
#     elif choice == "2":
#         car.drive()
#     elif choice == "3":
#         car.showDistanceDriven()
#     else:
#         continue