# Create a class Student that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the averge
print("Hello")
class Students :
    def __init__ (self,sub_1,sub_2,sub_3,marks_1,marks_2,marks_3):
        self.sub_1 = sub_1
        self.sub_2 = sub_2
        self.sub_3 = sub_3
        self.marks_1 = marks_1
        self.marks_2 = marks_2
        self.marks_3 = marks_3
    def average (self) :
        print(f"Average of {self.marks_1} , {self.marks_2} and {self.marks_3} = {(self.marks_1 + self.marks_2 + self.marks_3)/3}")

student_1 = Students("a", "b", "c", 10,20,30)
student_1.average()