# Day 12 of Python, Practice questions related to file i/o 

# Question 1 

# Create a new file "practice.txt" using python. Add the following in it. 
# "Hi everyone 
# we are learning File i/o
# using Java
# I like programming in Java"

file_1 = open("sample.txt", "w")
file_1.write("Hi everyone \n we are learning File i/o \n using Python \n I like programming in Python")

# Solving question using with syntax approach
with open("practice.txt", "w") as f :
    f.write("Hi everyone \n we are learning File i/o \n using Python \n I like programming in Python")

# Write a function that replaces all the occurance of the Java with Python