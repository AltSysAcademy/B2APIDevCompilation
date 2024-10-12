'''
Review:
Part 1: Variables, Data Types, Casting
Part 2: Conditionals and Booleans
Part 3: Lists, Dictionaries, Functions
Part 4: Loops 

Part 5: Object Oriented Programming
'''

# Variables
# Containers of Data (String, Integer, Float, Boolean, List, Dictionary)
# FORMAT: varname = data
name = "Nino"
age = 20
pi = 3.14
isTall = False
fruits = ["Apple", "Banana", "Cherry"]
account = {
    "name": "Nino Dulay",
    "age": 20,
    "hobby": "Programming"
}

# Casting
# Process of converting a data type to another data type
# FORMAT: new_data(old_data)
# String to Integer
# a = "20"       # STRING VERSION
# b = int(a)     # CONVERTED 
# print(b + 10)


'''
Booleans - Operators
Operators are used to compare and to create logic 

Operators: Logical, Comparison

Comparison: <, >, <=, >=, !=, ==
Logical: AND, OR, NOT
'''
# print(10 <= 10)

# AND - DAPAT LAHAT TRUE
# print(True and True) # True
# print(True and False) # False
# print(False and False) # False
# print(False and True) # False

# OR - KAHIT ISA LANG ANG MAGING TRUE
# print(True or True) # TRUE
# print(True or False)  # TRUE
# print(False or False)  # FALSE
# print(False or True) # TRUe

# NOT - Kapag True, magiging False
# print(not(True)) # False
# print(not(False)) # True


# Conditional Statement 
# Creating branches of logic in our code
# a = 5
# b = 5

# if a > b:
#     print("Good Morning!")
# elif a < b:
#     print("Good Evening!")
# else:
#     print("Good Afternoon!")

####
# List
# List is a container for multiple data (Store more than 1 data with different data types)
# FORMAT: var = [data1, data2, data3]

# fruits = ["Apple", "Banana", "Cherry"]


# Indexing
# Selecting specific item/element from a list
# By index position
# FORMAT: list[index]
#index:     0          1        2
# fruits = ["Apple", "Banana", "Cherry"]
# print(fruits[2])


# CRUD - Create, Read, Update, Delete
# C - Create (Append, Insert)
# FORMAT: list.append(new_data)  - ADDS DATA TO THE END OF THE LIST
# fruits = ["Apple", "Banana", "Cherry"]
# fruits.append("Dragonfruit")
# print(fruits)

# FORMAT: list.insert(index, new_data) - ADD DATA IN THE START OR THE MIDDLE
# fruits = ["Apple", "Banana", "Cherry"]
# fruits.insert(0, "Watermelon")
# print(fruits)

# R - READ (Indexing)
# FORMAT: list[index]
#index:     0          1        2
# fruits = ["Apple", "Banana", "Cherry"]
# print(fruits[2])

# U - UPDATE
# FORMAT: list[index] = new_data
# fruits = ["Apple", "Banana", "Cherry"]
# fruits[2] = "Watermelon" 
# print(fruits)

# D - DELETE (pop and remove)
# POP METHOD
# FORMAT: list.pop(index)
# fruits = ["Apple", "Banana", "Cherry"]
# fruits.pop(1)
# print(fruits)

# REMOVE METHOD
# FORMAT: list.remove(data)
# fruits = ["Apple", "Banana", "Cherry"]
# fruits.remove("Banana")
# print(fruits)

# By using del, you could only use index
# fruits = ["Apple", "Banana", "Cherry"]
# del fruits[0]
# print(fruits)

# Dictionary
# CRUD 
account = {
#    key   : value
    "name" : "Nino",
    "age"  : 20,
    "hobby": "Gaming"
}

# C - Create
# Add a new key-value pair
# FORMAT: dict.update({key:value})
# account.update({"password": "1234", "email": "altisjessienino18@gmail.com"})
# print(account)

# FORMAT: dict[new_key] = new_value
# account["password"] = "1234"
# account["email"] = "altisjessienino18@gmail.com"
# print(account)


# R - Read
# FORMAT: dict[key]
# print(account["name"])
# print(account["age"])

# U - Update
# Update a new key-value pair
# FORMAT: dict.update({key:value})
account = {
#    key   : value
    "name" : "Nino",
    "age"  : 20,
    "hobby": "Gaming"
}

# account.update({"hobby": "Programming"})
# print(account)

# FORMAT: dict[new_key] = new_value
# account["hobby"] = "Programming"
# print(account)

# D - Delete
# FORMAT: dict.pop(key)
# account.pop("hobby")
# print(account)

# del account["hobby"]
# print(account)

