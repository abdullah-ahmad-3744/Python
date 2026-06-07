print("Day 17 of learning Python")

class Students :
    def __init__(self, name) :
        self.name = name


std_1 = Students("Muhammad Abdullah")
std_2 = Students('Ali Ahmad')
print(std_1.name)
# deleting a property of an object
del std_1.name
print(std_1.name)
# deleting an object
del std_2
print(std_2)