# File I/O in Python
# I/O Syntax in Python

# Reading file
file_1 = open("demo.txt", "r")
print(file_1.read())


# Reading the specific or limited number of characters 
file_2 = open("demo.txt", "r")
print(file_2.read(7))

# Reading the file line by line
# First line 
line_1 = file_2.readline()
print("First Line in Demo File = ",line_1)

# Reading 2nd line in a file
second_line = file_2.readline()
print("Second Line ====== ", second_line)
file_1.close()
file_2.close()

#  Write operation 
file_2 = open("demo.txt", "w")
file_2.write("I am updating the Python file and erasing all the previous text.")
file_2.close()