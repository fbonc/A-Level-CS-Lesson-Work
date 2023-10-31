from math import sqrt
from copy import deepcopy

class Matrix:
    def __init__(self, *rows):
        self.matrix = [list(row) for row in rows]
        if not all(len(row) == len(self.matrix[0]) for row in self.matrix): 
            raise Exception("All rows must have the same number of columns")
        self.nrows = len(self.matrix)
        self.ncolumns = len(self.matrix[0])

    def __str__(self):
        return '\n'.join(map(str, self.matrix))
    
    def __add__(self, other):
        if self.nrows != other.nrows or self.ncolumns != other.ncolumns:
            raise Exception("Matrices must have same number of columns and rows for addition")
        
        result = deepcopy(self)
        for i in range(result.ncolumns):
            for j, k in zip(result.matrix, other.matrix):
                j[i] += k[i]
        return Matrix(*result.matrix)
    
    def __sub__(self, other): 
        if self.nrows != other.nrows or self.ncolumns != other.ncolumns:
            raise Exception("Matrices must have same number of columns and rows for subtraction")
        
        result = deepcopy(self)
        for i in range(result.ncolumns):
            for j, k in zip(result.matrix, other.matrix):
                j[i] -= k[i]
        return Matrix(*result.matrix)
    
    def __mul__ (self, other):
        if self.nrows != other.nrows or self.ncolumns != other.ncolumns:
            raise Exception("Matrices must have same number of columns and rows for multiplication")
        
        result = deepcopy(self)
        for i in range(result.ncolumns):
            for j, k in zip(result.matrix, other.matrix):
                j[i] *= k[i]
        return Matrix(*result.matrix)
    
    def __rmul__(self, other):
        result = deepcopy(self)
        for i in range(result.ncolumns):
            for j in result.matrix:
                j[i] *= other
        return Matrix(*result.matrix)
    
    def __eq__(self, other):
        if self.nrows != other.nrows or self.ncolumns != other.ncolumns:
                return False
        for i in range(self.ncolumns):
            for j, k in zip(self.matrix, other.matrix):
                if j[i] != k[i]:
                    return False
        return True


class Vector(Matrix):
    def __init__(self, *coefficients):
        super().__init__(*coefficients)

    def magnitude(self):
        return round(sqrt(sum(i**2 for i in self.matrix[0])))


def vectorTest():
    v1 = Vector((3, 4))

    print(f"Expecting 5 for magnitude of {v1}: ")
    assert v1.magnitude() == 5
    print("OK\n\n")

def matrixTest():
    m1 = Matrix((3, 4), (9, 1), (8, 7))
    m2 = Matrix((6, 1), (8, 2.5), (-6, 3.5))

    print(f"---Testing---\n{m1}\nand\n{m2}\n---\n")

    print(f"Expecting Matrix((9, 5), (17, 3.5), (2, 10.5)) for addition: ")
    assert Matrix((9, 5), (17, 3.5), (2, 10.5)) == m1 + m2
    print("OK\n")

    print(f"Expecting Matrix((-3, 3), (1, -1.5), (14, 3.5)) for subtraction: ")
    assert Matrix((-3, 3), (1, -1.5), (14, 3.5)) == m1 - m2
    print("OK\n")

    print(f"Expecting Matrix((18, 4), (72, 2.5), (-48, 24.5)) for multiplication: ")
    assert Matrix((18, 4), (72, 2.5), (-48, 24.5)) == m1 * m2
    print("OK\n\n")

    print(f"Expecting Matrix((12, 16), (36, 4), (32, 28)) for reverse multiplication (4 * m1): ")
    assert Matrix((12, 16), (36, 4), (32, 28)) == 4 * m1
    print("OK\n\n")

    print(f"Expecting 'Not equal' for m1 and m2")
    assert m1 != m2
    print("OK\n\n")

    print(f"Expecting 'Equal' for m1 == m1")
    assert m1 == Matrix((3, 4), (9, 1), (8, 7))
    print("OK\n\n")


v1 = Vector([2,8,-4])

print(v1.magnitude())



#--------- Old vector class that isn't a subclass of Matrix ---------

'''
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
            return Vector(*[i - j for i, j in zip(self.coefficients, other.coefficients)])
    
    def __mul__ (self, other):
        if self.dimension != other.dimension:
            print("ERROR: Vector dimensions must match for multiplication")
        else:
            return Vector(*[i * j for i, j in zip(self.coefficients, other.coefficients)])
    
    def __rmul__(self, other):
        return Vector(*[i * other for i in self.coefficients])
    
    def __eq__(self, other):
        if self.dimension != other.dimension:
            return False
        return all(i == j for i, j in zip(self.coefficients, other.coefficients))

    def magnitude(self):
        return round(sqrt(sum(i**2 for i in self.coefficients)))
'''

#--------- Old vector test ---------

'''

def vectorTest():
    v1 = Vector((3, 4))
    v2 = Vector((-6, 3.5))

    print(f"---Testing {v1} and {v2}---")

    print(f"Expecting (-3, 7.5) for addition: ")
    assert Vector((-3, 7.5)) == v1 + v2
    print("OK\n")

    print(f"Expecting (9, 0.5) for subtraction: ")
    print(v1)
    assert Vector((9, 0.5)) == v1 - v2
    print("OK\n")

    print(f"Expecting (-18, 14) for multiplication: ")
    assert Vector((-18, 14)) == v1 * v2
    print("OK\n\n")

    print(f"Expecting (12, 16) for reverse multiplication [4 * (3, 4)]: ")
    assert Vector((12, 16)) == 4 * v1
    print("OK\n\n")

    print(f"Expecting 5 for magnitude of {v1}: ")
    assert v1.magnitude() == 5
    print("OK\n\n")

'''


