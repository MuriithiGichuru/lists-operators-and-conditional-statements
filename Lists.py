# # a list is a collection of more than 1 variable
# I have more that 1 variable.. eg
# name = "muriithi gichuru"
# age = "34"
# location = "Nairobi"
# school = "RMIT"
# job = "unemployed"
#create 1 varialble
#person  = "" # this is a string
#we use square brackets to tell pythin that this is a list
person1 = []
print(type(person1))
#now we make a listy of my properties:
person1 = [10.0,"Muriithi Gichuru",25,"Nairobi","RMIT","Unemployed"]
print(person1)
#A list can store anything including another list. (as above, you have a float, string,integer, etc)

# positioning or indexing to access various items in a list
front_row_students = ["Said","Howard","Hajib","Kelvin"]
print(front_row_students)
#We now want to get the 1st student. NB in programming the 1st postion is 0
first_Student = front_row_students[0]
print(first_Student)
#if you have a long list and you want the last student, you note it as -1. second last student is -2 etc.
# NB; note from the last starts from -1 but from the front it starts from 0
first_Student = front_row_students[-1]
print(first_Student)

#List slicing
#if you have to select the 1st 2 students you use ranges
first_Student = front_row_students[0:2] # In this case, youd think you will say 0:1 to get the top 2 however in python, you need to go to the next number which is excluded
print(first_Student)
#in indexing,
# the integer at the left of the : is normally the starting point
# the integer at the right of the : is normaly the last list item but exclusive (i.e that last element is not included in the slice)

first_Student = front_row_students[1:3]
print(first_Student)

#List Operations
#Concatenating a list
form1east = ["Howard"]
form1west = ["Melvin"]
form1 = form1east + form1west
print(form1)
#find out the total number in a list. we use len (length of list)
print(len(form1))
#Find out if Melvin is on the list
is_Melvin = "Melvin" in form1
print(is_Melvin)

#Assignment
#List methods
#write - form1. and find out whats the list methods are. - append, extend, pop,
animallist = ['cow','goat','monkey','cow','sebra']
print(animallist)
animallist.append('dog')
print(animallist)
animallist.count('cow')
print(animallist.count('cow'))
animallist.copy()
print(animallist,copyright())
animallist2 = ['rabbit','chicken','hyena']
animallist.extend(animallist2)
print(animallist)
animallist.extend('antelope')
print(animallist)

