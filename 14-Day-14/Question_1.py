# Create a class Student that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the averge
class Students :
    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks
         
    def get_average (self) :
        print((self.marks[0] +  self.marks[1] +  self.marks[2])/ len(self.marks))

student_1 = Students("Abdullah Ahamad", [10,20,30])
student_1.get_average()