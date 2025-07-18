"""Q6: Create a class Vector that overloads:
 + for vector addition
 * for scalar multiplication

 == to compare two vectors
Also define a __str__() method for clean output."""

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
    

    def __mul__(self, scaler):
        return (self.a * scaler, self.b * scaler)
    
    def __eq__(self,other):
        return self.a == other.a and self.b == other.b

    def __str__(self):
        return f"Vector({self.a}, {self.b})"

Vector1 = Vector(4,4)
Vector2 = Vector(7,8)  

print(Vector1 + Vector2)
print(Vector1 * 2)
print(Vector1==Vector2)
print(Vector1 == Vector(4,4))