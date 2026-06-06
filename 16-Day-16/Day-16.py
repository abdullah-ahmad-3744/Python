# Abstraction in Python

class Cars :
    def __init__ (self) :
        self.accelrator = False
        self.brk = False
        self.clutch = False
        self.grear  = 0
    
    def start_car (self) :
        self.accelrator = True
        self.clutch = True
        self.grear = 1
        print("Car Started...")
    def stop_car (self) :
        self.accelrator = False
        self.brk = True
        self.clutch = True
        print("Car stopped...")


car_1 = Cars()
car_1.start_car()
print("=========================================================")
car_1.stop_car()

# Create an Account class with two attributes , account number and balance. Create methods for debt, credit and priting balance.


