# -------------------------
# Advance Oops Concept
# -------------------------
# Decorator

# def extragreeting(func):
#     def wrapper():
#         print("Hello from the Team Hitesh")
#         func()
#         print("Thankyou Visit Again")
    
#     return wrapper

# @extragreeting
# def greetings():
#     print("Welcome to Hitesh Team....")
    
# greetings()



# -------------------------
# Using *args and *kwargs
# -------------------------
# *args
# def addition(*args):
#     s = 0
#     for i  in args:
#         s = s + i
        
#     return s

# print(addition(10, 20, 30, 40, 50, 60, 70, 80))


# # **kwargs
# def info(**kwargs):
#     return kwargs

# print(info(name = "Hitesh", age = 19, profession = "Student"))


# ----------------------------
# One-Liners & Comprehensions
# ----------------------------
# # One-Liners

# a = 20
# print("Even number") if a % 2 == 0 else print("Odd number")


# # Comprehensions
# List
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# b = [i  for i in a if i % 2 == 0]

# print(b)


# Dict
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# square = {i: i **2 for i in a}

# print(square)


# Set
# a = [1, 2, 3, 4, 5, 6, 7, 8, 2, 5, 7, 10, 11, 9, 10, 11, 12, 13, 14, 15]

# unique = {i % 3 for i in a}

# print(unique)



# ----------------------------
# Lambda-Functions
# ----------------------------

# check = lambda x: "even number" if x % 2 == 0 else "odd number"

# print(check(11))


# addition = lambda a,b : a + b

# print("Total is : ", addition(10, 20))



# ----------------------------
# map(), filter(), zip()
# ----------------------------
# # map()
# a = ["Hitesh", "Akash", "Aryan", "Sarthak"]

# lenghts = list(map(len, a))

# print("length is :", lenghts)


# # celsius to fahrenheit
# temp_cel = [0, 20, 30, 35]

# temp_far = list(map(lambda x : (x * 9/5) + 35, temp_cel))

# print(temp_far)



# filter()
# marks = [23, 45, 40, 43, 78, 90, 11]

# passed = list(filter(lambda x : x >= 40, marks))

# print(passed)


# zip()
# name = ["Hitesh", "Akash", "Aryan", "Sarthak"]

# marks = [23, 45, 40, 43]

# result = list(zip(name, marks))

# print(result)