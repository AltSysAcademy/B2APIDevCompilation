# Object Oriented Programming
# We use objects to create our code
# Objects are similar to data types, they have their own attributes and methods

'''
FORMAT:
class Object:
    CODE HERE
'''

# 1. Introduction
# 2. Constructors 
# 3. Attributes
# 4. Methods
# 5. Application

# Class vs Object
# Class are a blueprint for an object (Common Noun, Category)
# Object are the instance of a class (Proper Noun, Specific)


#### PART 1 - INTRODUCTION
# Creation of a class
class Human:
    pass

# Instantiation (Creating instance from a class)
# Using the class
# Creation of objects
# FORMAT: var = Class()
'''
human1 = Human()
human1.name = "Nino Dulay"
human1.age = 20
human1.hobby = "Gaming"

human2 = Human()
human2.name = "Altis Dulay"
human2.age = 21
human2.hobby = "Programming"

print(human1.name, human2.name)
'''

### PART 2 and 3: Constructors and Attributes
# In a constructor, we put the attributes
'''
class Human:
    # Class Variable
    life_span = 20

    # Constructor (__init__)
    def __init__(self, name, age, hobby):
        # attribute - merong self
        self.name = name
        self.age = age
        self.hobby = hobby


human1 = Human("Nino Dulay", 20, "Gaming")
human2 = Human("John Doe", 21, "Programming")

human1.life_span = 12
print(human1.life_span)
print(human2.life_span)
'''

### PART 4: Method
class Human:
    # Constructor (__init__)
    def __init__(self, name, age, hobby):
        # attribute - merong self
        self.name = name
        self.age = age
        self.hobby = hobby

    # Method - function sa loob ng class, self lagi ang first parameter
    def eat(self):
        print(f"{self.name} is currently eating.")
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old. I love {self.hobby}.")

    def sleep(self):
        print("This person wants to sleep")

    # How to exclude self from a method
    @staticmethod
    def anyfunction():
        print("Hello!!! Random function here!")

# human1 = Human("Nino Dulay", 20, "Gaming")
# human1.anyfunction()


## Part 5: Inheritance (Optional)
'''
class Animal:    # PARENT CLASS
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print("I am eating.")
    
    def sleep(self):
        print("I am sleeping.")

class Dog(Animal):   # CHILD CLASS
    def __init__(self, name, age, breed):
        # super() - Animal.__init__
        super().__init__(name, age)
        self.breed = breed

dog1 = Dog("Brownie", 5, "Aspin")
print(dog1.age)
'''

#####
# Star-args - Multiple Arguments
# def add(*args):
#     print(sum(args))
# add(2,3,41,3,4,10)


# Double star-kwargs - Multiple Keyword Argument
'''
def introduce(**kwargs):
    print(kwargs["age"])
    kwargs["hobby"]
    kwargs["password"]

introduce(name="Nino Dulay")
'''


### Part 5: Application
class Human:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def greetOther(self, other):
        #       human1.name               human3.name
        print(f"{self.name} says hello to {other.name}.")

    def eat(self):
        print(f"{self.name} is currently eating.")
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old. I love {self.hobby}.")

    def sleep(self):
        print("This person wants to sleep")

human1 = Human("Nino Dulay", 20, "Gaming")
human2 = Human("John Doe", 21, "Programming")
human3 = Human("Jane Doe", 22, "Playing Guitar")

human1.greetOther(human3)

