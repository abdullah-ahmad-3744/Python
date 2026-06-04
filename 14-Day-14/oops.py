print("OOP'S in Python ")

class Students:
    def __init__(self,name,age):
        print('Constructor of Class Student...')
        self.name = name
        self.age = age
        
student_1 = Students("Ali Ahmad", 24)
print("Studnet_1 name : ",student_1.name)
print("Student_1 age : ",student_1.age)