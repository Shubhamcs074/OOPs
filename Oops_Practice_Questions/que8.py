"""Q8: Create the following class structure:
 LivingBeing (base class)
 Animal and Plant inherit from LivingBeing
 Amphibian inherits from both Animal and Plant
Each class should have a method describe() that prints its identity.
Use super() to ensure all describe() methods in the hierarchy are called in order.
Demonstrate how Python resolves the method calls using MRO."""

class LivingBeing:
    def describe(self):
        print("I am a Living Being.")

class Animal(LivingBeing):
    def describe(self):
        super().describe()
        print("I am Animal")

class Plant(LivingBeing):
    def describe(self):
        super().describe()
        print("I am a Plant.")

class Amphibian(Animal, Plant):
    def describe(self):
        super().describe()
        print("I am Amphibian.")

frog = Amphibian()
frog.describe()

print(Amphibian.__mro__)
