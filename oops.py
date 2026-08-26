#Q-1

# class Student:
    
#     def __init__(self, name):
#         self.my_name = name
        
#     def display(self):
#         print("Name :", self.my_name)

        
# n = Student("Kishor")

# n.display()


#Q-2

# class car:
#     def __init__(self, brand, model):
#         self.car_brand = brand
#         self.car_model = model

#     def display(self):
#         print("Brand :", self.car_brand)
#         print("Model :", self.car_model)


# cars = car("Hyundai", "i20")
# cars.display()


#Q-3

# class faculty:
#     def __init__(self, name, course):
#         self.Name = name
#         self.Course = course

#     def display(self):
#         print("Name :", self.Name)
#         print("Course :", self.Course)
        
# fac = faculty("Hitesh", "Python")
# fac.display()


# #Q-4
# class Students:
#     def __init__(self, name, address):
#         self.Name = name
#         self.Address = address

#     def display(self):
#         print(self.Name, "-", self.Address)
        
# students = []
# students.append(Students("NAME", "ADDRESS"))
# students.append(Students("Hitesh", "Jaipur"))
# students.append(Students("Suresh", "Delhi"))
# students.append(Students("Chirag", "Noida"))
# students.append(Students("Rohan", "Pune"))

# for student in students:
#     student.display()


##Q-5
# class University:
#     name = input("Please Enter your name : ")
#     age = int(input("Enter your age : "))
    
#     def addmission(name, age):
#         print(name)
#         print(age)
        
#     def display():
#         print("Your Addmission is Successfully!!!")


# add = University()
# University.display()


## Inheritance - Single Inheritance
## Base class (Parent class) = 1
## Child class (Derived Class) = 1

# class Animal: # Parent Class
#     def sounds(self):
#         print("Animal makes sound.")
        
    
# class Dog(Animal): # Derived Class
#     def sounds(self):
#         print("Dog barks.")
#     # pass


# d = Dog() # d is object
# d.sounds() # Output: Animal makes sound.


##Q-6
# class Animal():
#     def display(self):
#         print("Bull Dog")
    
# class Dog(Animal):
#     def bark(self):
#         print("Woof! Woof!")
        

# d = Dog()
# d.display()
# d.bark()


##Q-7
# class Person():
#     def show_name(self):
#         print("Name - Suresh")
        
# class Student(Person):
#     def show_details(self):
#         print("Roll no. :", 1234)
        

# s = Student()
# s.show_name()
# s.show_details()


##Q-8
# class vehicle():
#     def vehicle_brand(self):
#         print("Brand - Hyundai")
#         print("Brand - Hyundai")
#         print("Brand - Hyundai")
#         print("Brand - Hyundai")
        
# class vehicle_model(vehicle):
#     def model(self):
#         print("Model - i20")
#         print("Model - i10")
#         print("Model - creata")
#         print("Model - venue")
        
# v = vehicle_model()
# v.vehicle_brand()
# v.model()


##Q-9
# class account():
#     def __init__(self, acc_number, balance):
#         self.balance = balance
#         self.acc_number = acc_number
        
# class saving_acc(account):
#     def deposit(self, amount):
#         self.balance += amount
        
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient balance")

#     def display(self):
#         print("Account Number : ", self.acc_number)
#         print("Balance : ", self.balance)
        
# acc = saving_acc(1234, 5000)
# acc.deposit(2000)
# acc.display()
# acc.withdraw(1000)
# acc.display()

    

# ## Employee Management System

# class Person():
#     def __init__(self, name, age):
#         self.Name = name
#         self.Age = age

#     def display(self):
#         print("Name :", self.Name)
#         print("Age :", self.Age)
            
            
# class Employee(Person):
#     def __init__(self, name, age, employee_id, salary):
#         super().__init__(name, age)
#         self.Employee_id = employee_id
#         self.salary = salary
        
#     def display_1(self):
#         print("Employee_id :", self.Employee_id)
#         print("Salary :", self.salary)
            
# class Manager(Employee):
#     def __init__(self, name, age, employee_id, salary, department, bonus):
#         super().__init__(name, age, employee_id, salary)
#         self.Dept = department
#         self.bonus = bonus
        
    
#     def display_2(self):
#         print("Department :", self.Dept)
#         print("Bonus :", self.bonus)
#         final_salary = self.salary + self.bonus
#         print("\nFinal Salary with bonus :", final_salary)
        
        
# p = Person("Hitesh", 20)
# p.display()

# print()

# e = Employee("Hitesh", 20, 101, 50000)
# e.display_1()

# print()

# m = Manager("Hitesh", 20, 101, 50000, "IT", 15000)
# m.display_2()



# Multilevel Inheritance

# class Grandfather:
#     def house(self):
#         print("Grandfather's house.")

# class Father(Grandfather):
#     def car(self):
#         print("Father's car.")

# class Son(Father):
#     def bike(self):
#         print("Son's bike.")


# s = Son()

# s.car()
# s.bike()
# s.house()



# Multiple Inheritance

# class Father:                           # Parent Class / Base Class
#     def income(self):
#         print("Father's income.")

# class Mother:                           # Parent Class / Base Class
#     def power(self):
#         print("Every mother has more power.")

# class Brother:                          # Parent Class / Base Class
#     def tevar(self):
#         print("Brother is rowdy.")

# class Me(Brother, Father, Mother):      # Child Class / Derived Class
#     def myself(self):
#         print("I'm a good boy.")


# c = Me()        # Child class's object
# m = Mother()    # Parent class's object (Mother)
# b = Brother()

# c.income()
# c.power()
# c.tevar()
# c.myself()




## Q-1
# class Student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno

#     def show(self):
#         print("Name: ", self.name)
#         print("Rollno: ", self.rollno)

# class Marks:
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def calc(self):
#         total = self.m1 + self.m2 + self.m3
#         return total

# class Result(Student, Marks):
#     def __init__(self, name, rollno, m1, m2, m3):
#         Student.__init__(self, name, rollno)
#         Marks.__init__(self, m1, m2, m3)

#     def result(self):
#         total = self.calc()
#         print("Total marks: ", total)
#         avg = (total * 100) / 300
#         print("Result: ",f"{avg:.2f}","%")


# r = Result("Hitesh", 300, 90, 98, 92)

# r.show()
# r.result()



## Q-2
# class Employee:
#     def __init__(self, emp_name, emp_id):
#         self.emp_name = emp_name
#         self.emp_id = emp_id

#     def show(self):
#         print("Employee Name :", self.emp_name)
#         print("Employee Id :", self.emp_id)
        

# class Developer(Employee):
#     def __init__(self, language):
#         self.language = language
        
#     def display(self):
#         print("Programming langauge :", self.language)


# class Senior_Developer(Developer):
#     def __init__(self, experience):   
#         self.Experience = experience
        
#     def SD(self):
#         print("Year of experience :", self.Experience)
        


# e = Employee("Hitesh", 101)
# e.show()

# d = Developer("Python")
# d.display()

# s = Senior_Developer("5+year")
# s.SD()

        

##Que.Multiple inheritance

# class father:
#     def __init__(self, name):
#         self.Name = name

#     def show(self):
#         print("Father name is :", self.Name)
        
# class mother:
#     def __init__(self, name1):
#         self.Name = name1

#     def show1(self):
#         print("Mother name is :", self.Name)
        
# class child(father, mother):
#     def __init__(self, name, name1):
#         father.__init__(self, name)
#         mother.__init__(self, name1)
        
#     def display(self):
#         print("Child name is : Rohan")
        
        
# c = child("Rajesh", "Sunita")
# c.show()
# c.show1()
# c.display()



##Que.Multilevel inheritance

# class Person:
#     def __init__(self, name, age):
#         self.Name = name
#         self.Age = age

#     def display_person(self):
#         print("Name :", self.Name)
#         print("Age :", self.Age)
        

# class Student(Person):
#     def __init__(self, roll_no, course):
#         self.Roll_no = roll_no
#         self.Course = course

#     def display_student(self):
#         print("Roll_No :", self.Roll_no)
#         print("Course :", self.Course)
        
# class Branch(Student):
#     def __init__(self, branch):
#         self.Branch = branch
    
#     def display_branch(self):
#         print("Branch :", self.Branch)
        

# p = Person("Hitesh", 19)
# p.display_person()

# s = Student(1001, "BTech")
# s.display_student()

# b = Branch("AI & DS")
# b.display_branch()



# Question 1 — Basic Multiple Inheritance

# Create three classes:

# Father → method father_property()
# Mother → method mother_property()
# Child → inherit from both Father and Mother

# Create an object of Child and call both parent methods.


# class father:
#     def __init__(self, prop):
#         self.Property = prop
        
#     def father_property(self):
#         print("Father Property :", self.Property)
        
# class mother:
#     def __init__(self, mother_property):
#         self.Mother_property = mother_property
        
#     def mother_property(self):
#         print("Mother property :", self.Mother_property)
        
# class child(father, mother):
#     def __init__(self, prop, mother_property):
#         father.__init__(self, prop)
#         mother.__init__(self, mother_property)
        
#     def display(self):
#         print("Name : rohan")
        
        
# c = child(1000, 20000)
# c.father_property()
# c.mother_property()
# c.display()




# class Calculator:

#     def add(self, a, b, c=0):
#         return a + b + c

# c = Calculator()

# print(c.add(10, 20))
# print(c.add(10, 20, 30))



##====Duck Typing====
##Ex.
# class Dog:
#     def sound(self):
#         print("Bark")
        
# class Cat:
#     def sound(self):
#         print("Meow")
        
# def make_sound(animal):
#     animal.sound()
    
# dog = Dog()
# cat = Cat()

# make_sound(dog)
# make_sound(cat)


##====Overriding====
##Ex.
# class Animal:
#     def sound(self):
#         print("yyyyy")
    
# class Dog(Animal):
#     def sound(self):
#         print("bark")
    
# class Cat(Animal):
#     def sound(self):
#         print("meow")
        
# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()


##====Method Overloading====
##Ex.
# class Calculator:

#     def add(self, a, b, c=0):
#         return a + b + c
    
# c = Calculator()
# print("First add 1 and 2 :", c.add( 1, 2))
# print("second add 1, 2 and 3 :", c.add( 1, 2, 3))


##====Operator Overloading====
##Ex.
# class Student:
#     def __init__(self, marks):
#         self.marks = marks

#     def __add__(self, other):
#         return self.marks + other.marks
    
# s1 = Student(10)
# s2 = Student(20)

# print("Total is :", s1 + s2)



#Q-1
# Hybrid Inheritance

# class Person:
#     def name(self):
#         print("Person's name is XYZ")

# class Employee(Person):
#     def work(self):
#         print("Person is an employee in Amazon.")

# class Student(Person):
#     def study(self):
#         print("Person is a student of IIT Bombay")

# class TeachingAssistant(Employee, Student):
#     def teaching(self):
#         print("Person is teaching AI Engineering")

# t = TeachingAssistant()

# t.name()
# t.work()
# t.study()
# t.teaching()