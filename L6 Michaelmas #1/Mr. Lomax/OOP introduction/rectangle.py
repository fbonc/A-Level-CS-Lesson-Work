from math import sqrt

class Rectangle:
    def __init__(self, w, h):
        self._width = abs(w)
        self._height = abs(h)
    
    def __str__(self):
        return f"Rectangle of side lengths {self._width} and {self._height}"
    
    def getArea(self):
        area = round(self._width * self._height, 3)
        return area

    def getPerimeter(self):
        perimeter = round((self._width * 2) + (self._height * 2), 3)
        return perimeter
    
    def getDiagonal(self):
        diagonal = round(sqrt(self._width**2 + self._height**2), 3)
        return diagonal

def test():
    rec1 = Rectangle(2, 2)
    rec2 = Rectangle(-5, 4)
    rec3 = Rectangle(3.1, 9)

    tests = [[rec1, 4, 8, 2 * sqrt(2)],
             [rec2, 20, 18, sqrt(5**2 + 4**2)],
             [rec3, 27.9, 24.2, sqrt(3.1**2 + 9**2)]]
    
    for test in tests:  
        rec = test[0]

        print(f"---{rec}---")
        print(f"Expecting {round(test[1], 3)} for area: ")
        assert round(test[1], 3) == rec.getArea()
        print("OK\n")

        print(f"Expecting {round(test[2], 3)} for perimeter: ")
        assert round(test[2], 3) == rec.getPerimeter()
        print("OK\n")

        print(f"Expecting {round(test[3], 3)} for diagonal: ")
        assert round(test[3], 3) == rec.getDiagonal()
        print("OK\n\n")

test()