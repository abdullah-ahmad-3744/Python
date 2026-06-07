print("Day 17 of learning Python")

class Students :
    def __init__(self, name) :
        self.name = name


std_1 = Students("Muhammad Abdullah")
std_2 = Students('Ali Ahmad')
print(std_1.name)
# deleting a property of an object
# del std_1.name
# print(std_1.name)
# deleting an object
del std_2
# print(std_2)


# Private and Public attributes

class Account :
    def __init__ (self, account_number, account_password) :
        self.account_number= account_number
        self.account_password = account_password

account_1 = Account(1234567890, 1122)
print("Account number : ",account_1.account_number)
print("Account password : ",account_1.account_password)