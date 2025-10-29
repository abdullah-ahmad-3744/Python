print("Hello World")
print("First Day of Python Programming")
# =======================================================

# Variables in Python
a = 10 
b = 20 
# Printing the values of a and b 
print ("Value of a : ",a)
print ("Value of b : ",b)



# Operators in Python
# Sum of a and b a+b
print ("Sum of", a , "and " , b, "= ",  a+b)
# Arithmatic Operators in Operators
first_number = 30 
second_number = 10 
# Addition of two numbers 
print ("Addition in Arithmatic Operators")
print( "Sum of",first_number, "and", second_number, "=",   first_number + second_number)
print()
# Subtraction of two number
print ("Subtraction in Arithmatic Operators")
print("Subtraction from", first_number, "of", second_number, "=", first_number - second_number)
print()
# Multiplication of two numbers
print ("Multiplication in Arithmatic Operators") 
print (first_number,"* by",second_number , "=" ,first_number * second_number)
print()
# Division of two numbers 
print ("Division in Arithmatic Operators")
print(first_number , "Divided by", second_number , "=", first_number / second_number)
print()
# Remainder of two numbers 
print ("Remainder in Arithmatic Operators")
print ("Remainder of",first_number, "% ", second_number, "=",first_number % second_number)
print()
# Power of numbers
print("Power Operator in Arithmatic Operator")
print(first_number,"Power ",second_number, "=",first_number ** second_number)
print()




# Relational or Comparision operators in Operators
# Equal to operator in Comparision operator
print ("Checking if",first_number, "is equal to", second_number,"=",first_number == second_number)
print()

# Not Equal to Operator in Comparision Operators
print("Checking if",first_number, "not equal to", second_number, "=",first_number != second_number)
print()

# Greater then Operator > in Comparision Operators
print(first_number, "Is Greater than", second_number, "=" , first_number > second_number )
print()

# Less then Operator > in Comparision Operators
print(first_number, "Is Less than", second_number, "=" , first_number < second_number )
print()


# Greater than Equal to (>=) Operator in Comparision Operator
print("Checking if",first_number, ">=",second_number, "=",first_number >= second_number)
print()

# less than Equal to (<=) Operator in Comparision Operator
print("Checking if",first_number, "<=",second_number, "=",first_number >= second_number)
print()



# Logical Operators in Operators
# Not Operator in Logical Operators
print("Not Operator negates or reverse the output from True to Flase and vice versa")
print(not True)
print(first_number > second_number)
print (not (first_number > second_number))
print()

# And operator in Logical Operators
print("And operator returns True only if both Conditions are Ture")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()

#  or Operator in Logical Operators
print("OR operator returns True only if only one Conditions is Ture from two conditions")
print(True  or True)
print(True  or False)
print(False or  True)
print(False or  False)
print()



# Conversion in Python
print("This is Type Conversion")
third_number = 10.5
# Int + Int 
print("int + int = int as ",first_number, "+", second_number, "=", first_number + second_number)
print()
# int + float
print("int + float = float as ",first_number, "+", third_number, "=", first_number + third_number)
print()
# int + str
name = "Muhammad Abdullah"
# print("int + str return type error", first_number + name)
print()

# int + boolean 
print("int + bool return int as",first_number ,"+",True , "=",first_number + True) 
print("int + bool return int as",first_number ,"+",False , "=",first_number + False) 
print()

# int + none
# print("int + none returns type error", first_number + None)
print()

# str + int 
# print("str + int returns type error",name + first_number)
print()

# str + str 
user_name2 = "Baloch"
print("str + str returns str  ", name +  " ",user_name2)
print()

# str + float
# print("str + float returns type error",name + third_number)
print()

# str + bool
# print("str + bool returns the type error",name + True)
print()