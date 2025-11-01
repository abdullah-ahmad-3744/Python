# Dictionaries in Python

dictionary1 = {
    "name" : "Muhammad Abdullah",
    "age" : 24,
    "city" : "Bahawalpur"
}

print(dictionary1)
print()

# Printing the value of a key
print("Name = ",dictionary1["name"])
print("Age = ",dictionary1["age"])
print()

dictionary2 = {
    "name" : "Ali Ahmad",
    "age" : 21,
    "marks" : {
        "English" : 82,
        "Physics" : 73,
        "Mathematics" : 90
        }
}
print("Makrs of ",dictionary2["name"], "=",dictionary2["marks"])
print("Marks in Physics = ", dictionary2["marks"]["Physics"])
print()


# Dictionary methods
# Most commonly used dictionary methods

print("The type of the Dictionary = ",type(dictionary1))
print()

print("Number of key-value pairs = ",len(dictionary2))
print()
print("Number of key-value pairs = ",len(dictionary2["marks"]))