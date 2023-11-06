class Yard:
    def __init__(self, *sidings):
        self._yard = sidings
    
    def __str__(self):
        msg = ''
        for i in range(len(self._yard)):
            msg += f"Siding {i + 1}\n"
        return msg

class Siding:
    def __init__(self):
        self._head = -1
        self._size = 0
        self._siding = [None] * 30
    
    def push(self, wagon):
        if self._size == 30:
            raise Exception("Cannot push to full stack")
        self._head += 1
        self._siding[self._head] = wagon
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise Exception("Cannot pop from empty stack")
        temp = self._siding[self._head]
        self._head -= 1
        self._size -= 1
        return temp

    def getSize(self):
        return self._size
    
    def __str__(self):
        msg = '--Back--\n'
        for i in self._siding:
            msg += f"{i._ownerName}'s Wagon\n"
        msg += '--Exit/Entrance--'
        return msg

class Wagon:
    def __init__(self, ownerName: str, weight: int, numberOfWheels: int):
        self._ownerName = ownerName
        self._weight = weight
        self._numberOfWheels = numberOfWheels

    def __str__(self):
        return f"Type: normal, owner name: {self._ownerName}, weight: {self._weight}, number of wheels: {self._numberOfWheels}"

    def getOwnerName(self):
        return self._ownerName

class OpenWagon(Wagon):
    def __init__(self, ownerName: str, weight: int, numberOfWheels: int):
        super().__init__(ownerName, weight, numberOfWheels)
        self._type = "Open Wagon"
    
    def __str__(self):
        return f"Type: {self._type}, owner name: {self._ownerName}, weight: {self._weight}, number of wheels: {self._numberOfWheels}"

class ClosedWagon(Wagon):
    def __init__(self, ownerName: str, weight: int, numberOfWheels: int, height: int, numberOfDoors: int, suitableForFoodStuffs: bool):
        super().__init__(ownerName, weight, numberOfWheels)
        self._height = height
        self._numberOfWheels = numberOfWheels
        self._type = "Closed Wagon"

    def __str__(self):
        return f"Type: {self._type}, owner name: {self._ownerName}, weight: {self._weight}, number of wheels: {self._numberOfWheels}, height: {self._height}"

if __name__ == "__main__":

    #pushing siding test
    import random as rd
    siding1 = Siding()
    for i in range(30):
        wagon = Wagon(f"Person {i + 1}", rd.randint(500, 1000), rd.randint(4,8))
        siding1.push(wagon)
    if input("Try pushing siding test? (y/n) ") == "y":
        print(f"{siding1}\n")

    #max size test
    if input("Try max size test for siding? (y/n) ") == "y":
        siding1.push(Wagon("MAX", 0, 0))

    #popping siding test
    if input("Try popping test for siding? (y/n) ") == "y":
        for i in range(30): print(f"{siding1.pop().getOwnerName()}'s Wagon")
        print('')
    else:
        for i in range(30): siding1.pop()

    #retrieving from empty sliding test
    if input("Try empty test for siding? (y/n) ") == "y":
        siding1.pop()

    #yard testing
    if input("Try yard test? (y/n) ") == "y":
        s1 = Siding()
        s2 = Siding()
        s3 = Siding()

        yard = Yard(s1, s2, s3)
        print(yard)
        print('')

    #wagon classes testing
    if input("Try wagon classes test? (y/n) ") == "y":
        openWagon = OpenWagon("Jeffrey", 756, 4)
        closedWagon = ClosedWagon("Rys", 560, 8, 2, 2, True)

        print(f"Open wagon details: {openWagon}")
        print(f"Closed wagon details: {closedWagon}")