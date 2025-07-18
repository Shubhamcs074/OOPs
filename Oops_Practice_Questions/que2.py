"""Q2: Create a Student class with private attributes for name, roll_no, and marks. Add setter methods
that validate:
 Marks must be between 0 and 100.
 Name must be alphabetic only.
Implement a method get_grade() based on marks."""

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = None  
        self.__roll_no = roll_no  
        self.__marks = None  
        
        
        self.set_name(name)
        self.set_marks(marks)

    
    def set_name(self, name):
        if name.isalpha():  
            self.__name = name
        else:
            print("Invalid name.")

    
    def set_marks(self, marks):
        if 0 <= marks <= 100:  
            self.__marks = marks
        else:
            print("Invalid marks.")

    
    def get_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 50:
            return "C"
        elif self.__marks >= 35:
            return "D"
        else:
            return "F"
    
    
    def display_student_info(self):
        print(f"Student Name: {self.__name}")
        print(f"Roll Number: {self.__roll_no}")
        print(f"Marks: {self.__marks}")
        print(f"Grade: {self.get_grade()}")


student1 = Student("Vikas", 101, 85)
student1.display_student_info()

student2 = Student("Ram123", 102, 110) 
student2.display_student_info()

student3 = Student("Ravi", 103, 40)
student3.display_student_info()
