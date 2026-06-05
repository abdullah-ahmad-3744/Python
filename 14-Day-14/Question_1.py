# Create a class Student that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the averge
class Students :
    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks
         
    def get_average (self) :
        marks = self.marks
        sum =  0
        for i in marks:
            sum += i
        average = sum / len(marks)
        print(f"Average of {marks[0]}, {marks[1]} and {marks[2]} = {average}")
student_1 = Students("Abdullah Ahamad", [10,20,30])
student_1.get_average()