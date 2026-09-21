# #STRING -> String is a collection of character.

# name = "Hitesh Kumar Suthar"
# n = name.replace("Hitesh","Suresh")
# print(n)


# #1.Concatenation
# str_1 = "Hitesh"
# str_2 = "Kumar"
# str_3 = "Suthar"

# str_4 = str_1 + " " + str_2 + " " + str_3
# print(str_4)


# #2.Repetition
# name = "offer"
# print(name * 100)

# a = "Hiteshkumarsuthar"

# print(a[len(a)-1]) #print(a[34-1]) = print(a[33]) = 

# print(a[0 : -1]) #using indexing to print unkown string without length 

# print(a[ :: -1]) #using slicing to reverse string

# print(a[6 : 11]) #slicing


# #4.Imp. Methods --> find(), index(), split(), join()
# a = "Hitesh,kumar,suthar"

# print(a.find("t")) #index return
# print(a.index("t")) # index return

# print(a.count("t")) #total character number count

# b = a.split(",") #split
# print(b)
# print("/".join(b)) #join


##---PRACTICE---
##-1-
# number = "Hitesh, Suthar, Suresh, Chirag, Hitesh, Hitesh"

#(String convert to => list)
# print(number.split(", "))

# print(number.find("Suresh"))

# print(number.count("Hitesh"))

# print(number.replace("Hitesh", "Suresh"))

# print(number.strip())


##-2-
# item = "chai"
# quantity = 2
# order = "I orederd {} cup of {}"

# print(order.format(quantity, item))


##-3-
# item_veriety = ["Laptop", "mouse", "keyboard", "headphones"]

##(List convert to => string)
# print(", ".join(item_veriety))


##-4-
# name = "Hitesh Kumar Suthar"

# print(len(name))
# print("Hitesh" in name)

# for letter in name:
#     print(letter)
    

##Eg.
# path = r"c:/user/Hitesh/window11"
# print(path)

#-5-
# name = "Hitesh"

# for names in name:
#     if "Hitesh" in name:
#         print("True")
#     else:
#         print("False")
    
#-6-
# char = "hithehsh"
# print(char.count("h"))
# print(char.replace("h", "H"))

# #-7-
# name = "Python programming"

# #substring
# # print("python" in name)

# print(len(name))

# print(name)

# #remove duplicate value
# print("".join(set(name)))


#-8-
# name = "hitesh suthar"
# #first ch. upper
# text = name.title()
# print(text)
