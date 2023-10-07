class Value:
    def __init__(self, val):
        self.value = val
    
    def add(self, other):
        new_object = Value(self.value + other.value)
        return new_object
    
x = Value(3)
y = Value(4)

z = x.add(y)
print(z.value)