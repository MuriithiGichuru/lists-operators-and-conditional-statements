#Classes and objects

# Terminologies
#Class - A class is a group of related functions and variables
#object oriented programing -OOP -  you model a user and add function to that user
#object is a member of a class
#always ask yourself, who will use this function. then attach that function to the user who is an object. #

# Method - a function that is inside a class is called 'METHODS'
#OBJECT -  an instance of a class. its a 'member' of that class.
#its like an example of a class

#student =[] # student is an empty list
#we are saying that student is is member of class list

#a CONSTRUCTOR - 'It is a method but a special method that runs everytime you create an instance of a class
# everytime you instanciate a class.


#
# student = [] # to create a list
# student = {} # to create a dictionary
# student = () # to create a tupple

# when creating a class, it should start with a capital letter
class Student:
#we then want to give the class members. Students will always have:
     math = 0 # this shows math is an integer
     eng = 0
     sci = 0
     kis = 0
     ssr = 0
     total_marks = 0
     average = 0.0 # Makes average a float
     grade ='' # makes grade a string like A,B C
# the above are just properties
#we need to create methods(functions) within the class
#when defining the method, make it a verb like 'find'





     def find_total(self):
          self.total_marks = self.math+self.eng+self.sci+self.kis+self.ssr

     def find_average(self):
          self.average = self.total_marks/5

     def find_grade(self):
          ave = self.average
          if ave >= 80 and ave<=100:
               self.grade = 'A'
          if ave>=70 and ave<80:
               self.grade = 'B'
          if ave>=60 and ave<70:
               self.grade = 'C'
          if ave>=50 and ave<60:
               self.grade = 'D'
          else:
               self.grade = 'E'


     #a constructor
     def __init__(self,math,eng,kis,ssr,sci):
          self.math = math
          self.eng = eng
          self.kis = kis
          self.ssr = ssr
          self.sci = sci
          self.find_total()
          self.find_average()
          self.find_grade()


#
#
#
#
#
