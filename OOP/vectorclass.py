from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))
    
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return Vector(self.x, self.y)
    
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        print((self.x, self.y)) 
        return Vector(self.x, self.y)
    
    def __mul__ (self, other):
        self.x *= other.x
        self.y *= other.y
        return Vector(self.x, self.y)
    
    def __rmul__(self, other):
        self.x *= other
        self.y *= other
        return Vector(self.x, self.y)
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def magnitude(self):
        return round(sqrt(self.x**2 + self.y**2), 2)


def test():
    v1 = Vector(3, 4)
    v2 = Vector(-6, 3.5)

    print(f"---Testing {v1} and {v2}---")

    print(f"Expecting (-3, 7.5) for addition: ")
    assert Vector(-3, 7.5) == v1 + v2
    print("OK\n")

    print(f"Expecting (9, 0.5) for subtraction: ")
    assert Vector(9, 0.5) == v1 - v2
    print("OK\n")

    print(f"Expecting (-18, 14) for multiplication: ")
    assert Vector(-18, 14) == v1 * v2
    print("OK\n\n")

    print(f"Expecting 5 for magnitude of {v1}: ")
    assert v1.magnitude() == 5
    print("OK\n\n")

    print(f"Expecting 'Not equal' for {v1} == {v2}: ")
    assert v1 != v2
    print("OK\n\n")

test()