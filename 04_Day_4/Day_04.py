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
print()

# Accessing and Searching methods of Dictionary 
# keys() =====> returns all the keys of the dictionary
print(dictionary2.keys())
print()

# values() =====> retruns the values of the keys
print(dictionary2.values())
print()

# item() ====> returns the key-valaue pair as a separate tuple
print(dictionary1.items())
print()


print(dictionary2.items())
print()


# get() ====> returns the value of key and returns none if key is invalid
print(dictionary1.get("name"));
print(dictionary2.get("address"))
print()


# Adding and Updating methods

# update({key : value}) ====> updates the existing dictionary
dictionary1.update({"city" : "Lahore"})
dictionary1.update({"address" : ""})
print(dictionary1)
