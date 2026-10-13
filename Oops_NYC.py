#-----------------
# NYC with OOPS
#-----------------
print("Welcome to NYC with Oops")
#---------------------------
# Functional Programming
#---------------------------
# def add(a, b):
#     print(a+b);

# add(1, 2)
# add(2, 3)

#---------------------------
# Oops Programming
#---------------------------
#Define class, Attributes & methods
# class Car:
#     car_name = "BMW" # Attributes

#     def model(): # Methods
#         print("Car Model is X5")
  
  
# # You can access attributes and
# # methods after accessing the class

# print(Car.car_name) # accessing Attributes

# Car.model() # accessing methods

#---------------------------
# Objects
#---------------------------
# class Bag:
#     name = "Snax Bag"
    
#     def details(self):
#         print("This is a company who create bags")
        

# Instance Object
# wildcraft = Bag()
# Campus = Bag()

# # Accessing the attributes
# print(wildcraft.name)
# print(Campus.name)

# wildcraft.details()


#---------------------------
# Program-1
#---------------------------
# class Bag:
#     def __init__(self, material, zips, pocket):
#         self.material = material
#         self.zips = zips
#         self.pocket = pocket


# #Create object with the value
# reebok = Bag("leather", 1, 3)
# campus = Bag("polyster", 3, 4)

# #Access the attributes
# print(reebok.material)
# print(reebok.zips)
# print(reebok.pocket)
# print(campus.material)
# print(campus.zips)
# print(campus.pocket)


#---------------------------
# Program-2
#---------------------------
# class Student:
#     a = 12  # Class Attributes
    
#     def __init__(self, name):
#         self.name = name  # Object/Instance attributes
        
    
#     def hello(self):  # Instance/object method | capture the location of obj
#         print(f"How are you my name is {self.name}")
        
#     @classmethod
#     def details(cls): # Class method | capture the location of class
#         print(f"How are you my name is {cls.a}")
        

#     @staticmethod
#     def school(): # This is a static method and it will not target any location
#         print("Welcome to my school and I am a static method")
        
        
# obj = Student("Hitesh")
# print(obj.name)


# obj.details() # @classmethod call



#---------------------------
# Inheritence
#---------------------------
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Child(Animal):
#     pass


# obj = Animal("Dog")
# print(obj.name)

# obj1 = Child("Hitesh")
# print(obj1.name)


# print("Single-Inheritance")
#---------------------------
# Single-Inheritence
#---------------------------
# class BagFactory:
#     def __init__(self, material, zip, pocket):
#         self.material = material
#         self.zip = zip
#         self.pocket = pocket
        
#     def details(self):
#         print(self.material)
#         print(self.zip)
#         print(self.pocket)
        
# class Rebook(BagFactory):
#     def __init__(self, material, zip, pocket, color):
#         super().__init__(material, zip, pocket)
#         self.color = color
        
#     def details(self):
#         print(self.color)
#         return super().details()
    
    
# obj = Rebook("leather", 2, 3, "red")
# obj.details()


# print("Multilevel-Inheritance")
# #---------------------------
# # Multilevel-Inheritence
# #---------------------------
# class BagFactory:
#     def __init__(self, material, zip, pocket):
#         self.material = material
#         self.zip = zip
#         self.pocket = pocket
        
#     def details(self):
#         print(self.material)
#         print(self.zip)
#         print(self.pocket)
        
# class Rebook(BagFactory):
#     def __init__(self, material, zip, pocket, color):
#         super().__init__(material, zip, pocket)
#         self.color = color
        
#     def details(self):
#         print(self.color)
#         return super().details()

# class Campus(Rebook):
#     def __init__(self, material, zip, pocket, color):
#         super().__init__(material, zip, pocket, color)
        

# obj = Rebook("leather", 2, 3, "red")
# obj.details()


# print("Multiple-Inheritance")
# #---------------------------
# # Multiple-Inheritence
# #---------------------------
# class GrandParent:
#     def __init__(self, name):
#         self.name = name

# class Parent:
#     def __init__(self, age):
#         self.age = age

# class Child(GrandParent, Parent):
#     def __init__(self, name, age):
#         GrandParent.__init__(self, name)
#         Parent.__init__(self, age)
        
# obj = Child("Hitesh", 19)
# print(obj.name)
# print(obj.age)


# print("Polymorphism")
# #---------------------------
# # Polymorphism
# #---------------------------
# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")
    
# class Horse:
#     def sound(self):
#         print("Horse sound")
        
# obj = Dog()
# obj1 = Cat()
# obj2 = Horse()

# obj.sound()
# obj1.sound()
# obj2.sound()

# #-----------------------------------
# # Polymorphism 1)METHOD-OVER-RIDDING
# #-----------------------------------
# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def details(self):
#         print(f"My name is {self.name}")
        
# class child(Animal):
#     def details(self):
#         super().details()
#         print(f"My child name is {self.name}")
        
# obj = child("Hitesh")

# obj.details()

#-----------------------------------
# Polymorphism 1)METHOD-OVER-LOADING
#-----------------------------------
# # Using Default method
# class Parent:
#     def add(self, a, b, c=0):
#         print(a + b + c)

# obj = Parent()

# obj.add(10, 20)
# obj.add(10, 20, 30)



# --------------------
# Using (*args)
# --------------------
# class ARGS:
#     def add(self, *args):
#         print("SUM IS -> ", sum(args))
        
# obj = ARGS()

# obj.add(10, 20)
# obj.add(10, 20, 30)
# obj.add(10, 20, 30, 40)
# obj.add(10, 20, 30, 40, 50)
# obj.add(10, 20, 30, 40, 50, 60)
# obj.add(10, 20, 30, 40, 50, 60, 70)
# obj.add(10, 20, 30, 40, 50, 60, 70, 80)



# ----------------------------------------
# Using-Decorator (@singledispatchmethod)
# ----------------------------------------
# from functools import singledispatchmethod

# class Parent:
#     @singledispatchmethod
#     def add(self, value):
#         print("Default :", value)
        
#     @add.register
#     def _(self, value: int):
#         print("INT :", value)
        
#     @add.register
#     def _(self, value: str):
#         print("STR :", value)
        
# obj = Parent()
# obj.add(10)
# obj.add("Hello")


# --------------------
# Encapsulation
# --------------------
# class Factory:
#     def __init__(self, type, tyre, color):
#         self.type = type # Public object Attribute
#         self.__tyre = tyre # private object Attribute
#         self.__color = color # private object Attribute
        
#     def __details(self): # This is private method
#         print(self.type)
#         print(self.__tyre)
#         print(self.__color)
        
        
# obj = Factory("Sedan", "MRF", "BALCK")

# obj.__details()



# --------------------
# Abstraction
# --------------------

# from abc import ABC, abstractmethod

# class Car(ABC):  # Abstract class
#     @abstractmethod
#     def enginestart(self):  #Abstract method
#         pass
    
# class BMW(Car):
#     def enginestart(self):
#         print("Car Started...")

# class I20(Car):
#     def enginestart(self):
#         print("i20 is started...")
#         return super().enginestart()

# C = BMW()
# C.enginestart()

# I = I20()
# I.enginestart()



# --------------------
# Dunder Methods
# --------------------
# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def __str__(self):
#         return f"Hello my name is {self.name}"
    
    
# obj = Animal("Lion")
# print(obj)

# obj2 = Animal("Dog")
# print(obj2)


# __sub__ using dunder method
# class number:
#     def __init__(self, num):
#         self.num = num

#     def __sub__(self, other):
#         return self.num - other.num
    
    
# num1 = number(20)
# num2 = number(10)

# print(num1 - num2)


                                               
#----------------------------------------------------------------
# dir() -> Object ke methods aur attributes ke naam batata hai. -
# type() -> Object ka data type batata hai.                     -
#                                                               -
# a = 12                                                        -
# print(type(a))                                                -
# print(dir(a))                                                 -
#----------------------------------------------------------------


