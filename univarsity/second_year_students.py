from first_year_students import FirstYearStudents

class SecondYearStudents(FirstYearStudents):

    def __init__(self ,name , roll_nunber , subjects_name ):
        
        
        super().__init__(name , roll_nunber , subjects_name)

    def attendence(self):

        print(f" {self.name} is present")