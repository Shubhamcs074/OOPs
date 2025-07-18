"""Q7: Design a basic School Management System with:
 Person (base class)
 Teacher and Student (subclasses)
 Method display_details() implemented differently in each
 Use polymorphism to handle multiple objects"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_details(self):
        return f"Teacher : {self.name}, Age : {self.age}, Subject: {self.subject}"
    

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display_details(self):
        return f"Student Name : {self.name}, Age: {self.age}, Grade: {self.grade}"
    
teacher1 = Teacher("Mr. Vipul Sharma", 30, "Python Programming")
student1 = Student("Shubham", 20, "A+")

print(teacher1.display_details())
print(student1.display_details())