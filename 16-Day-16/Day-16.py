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

print("=========================================================================")
print()
print()
# Create an Account class with two attributes , account number and balance. Create methods for debt, credit and priting balance.

class Accounts :
    def __init__ (self, balance, acc) :
        self.account_number = acc
        self.balance = balance
        
    
    def debt (self,amount) :
        self.balance -= amount 
        print(f"{amount} rupees debited from your account : {self.account_number}")
        
    
    def credit (self,amount) :
        self.balance += amount
        print(f"{amount} is credited in your account")
    
    def print_balance (self) :
        print("Account balance : ", self.balance)
        
user_1 = Accounts(499999,1234567890)
user_1.debt(9999999999999999)
user_1.credit(2222222)
user_1.print_balance()