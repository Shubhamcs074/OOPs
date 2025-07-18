"""Q3: Create a class Person with name and age.
Create another class Employee with emp_id and designation.
Now create a class Manager that inherits from both and adds a method to display all details.
Demonstrate method resolution order (MRO)."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Employee:
    def __init__(self, emp_id, designation):
        self.emp_id = emp_id
        self.designation = designation

class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, designation):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, designation)

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Designation: {self.designation}")

manager1 = Manager("Mr. Vipul Sharma", 30, "A 420", "Head of Devlopers")

manager1.display_details()

print(Manager.__mro__)  
