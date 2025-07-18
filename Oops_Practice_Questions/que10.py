"""Q10: Simulate the diamond problem:
    Class A has a method display()
    Class B and C inherit from A and override display()
    Class D inherits from both B and C
   Call display() from an object of D and explain which one gets called and why (via MRO)."""
class First:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print(f"a has value in class First :{self.a}")
        print(f"b has value in class First :{self.b}")



class Second(First):
    def __init__(self, a, b, c):
        First.__init__(self, a, b)
        self.c = c

    def display(self):
        super().display()
        print(f"c has value in class Second:{self.c}")
        


class Third(First):
    def __init__(self, a, b, d):
        super().__init__(a, b)
        self.d = d

    def display(self):
        super().display()
        print(f"d has value in class Third:{self.d}")
        


class Fourth(Second, Third):
    def __init__(self, a, b, c, d):
        Second.__init__(self, a, b, c)
        Third.__init__(self, a, b, d)


    def display(self):
        super().display()
        print(f"Updated value of d in class Fourth:{self.d}")


head = Fourth("Ram", "Ajay", "Susmita", "Priya")

head.display()

print(Fourth.__mro__)
    

