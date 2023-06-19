"""
class Student:

    def __init__(self): # it is a constructor

        self.name = "francis "  # these three lines are attributes
        self.age = 45
        self.address = "Kishna colony (mhow)"

    def Read(self): # these two lines are methodes
        
        print(f"You are a good reader {self.name} ")

    def truth(self):

        print(f"I'm glad you tell the truth every time {self.name}")

    def year(self):
        print(f"I'm {self.age} years old.")
"""
#Another way to call attributes
"""import random

class Student:

    

    def __init__(self, name, age, address, Bottel_color): # it is a constructor

        self.name = name  # these three lines are attributes
        self.age = age
        self.address = address
        self.Bottel_color = Bottel_color

    def Read(self): # these two lines are methodes 
        
        print(f"You are a good reader {self.name} ")

    def truth(self):

        print(f"I'm glad you tell the truth every time {self.name}")

    def year(self):
        print(f"I'm {self.age} years old.")

    def test(self,topic):

        print(f"student {self.name} give a test of {topic}")

    def marks(self):

        return random.randint(1,100)"""


