
from student import Student
 
if __name__ == "__main__": # Always write a code like this

    francis = Student()

    print(francis.age)# This is how you can call Attribute of class
    print(francis.name)
    print(francis.roll_number)

    francis.Read() # this is how you can call method from class

    francis.speak()
