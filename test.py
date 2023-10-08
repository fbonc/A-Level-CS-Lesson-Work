from math import sqrt

class Vector:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)
        self.dimension = len(self.coefficients)

    def __str__(self):
        return str(tuple(self.coefficients))
    
    def __add__(self, other):
        if self.dimension != other.dimension:
            print("ERROR: Vector dimensions must match for addition")
        else:
            return Vector(*[i + j for i, j in zip(self.coefficients, other.coefficients)])
    
    def __sub__(self, other): 
        if self.dimension != other.dimension:
            print("ERROR: Vector dimensions must match for subtraction")
        else:
            return Vector(*(i - j for i, j in zip(self.coefficients, other.coefficients)))
    
    def __mul__ (self, other):
        if self.dimension != other.dimension:
            print("ERROR: Vector dimensions must match for multiplication")
        else:
            return Vector(*(i * j for i, j in zip(self.coefficients, other.coefficients)))
    
    def __rmul__(self, other):
        return Vector(*(i * other for i in self.coefficients))
    
    def __eq__(self, other):
        if self.dimension != other.dimension:
            return False
        return all(i == j for i, j in zip(self.coefficients, other.coefficients))

    def magnitude(self):
        return round(sqrt(sum(i**2 for i in self.coefficients)))
    

v1 = Vector(1, 3, 6, 7, 8)

v2 = Vector(8, 9, 10, 2, 3)

print(v1 + v2)
