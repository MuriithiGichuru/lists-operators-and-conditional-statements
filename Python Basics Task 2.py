 #TASK 2:
# Implement a function that takes as input three variables,
# and returns the largest of the three.
# Do this without using the Python max () function!
# The goal of this exercise is to think about some internals
# that Python normally takes care of for us

#Using the max function
# def size (a,b,c):
#     return max(a,b,c)
#
#
# length = eval(input('enter length in cm'))
# width = eval(input('enter width cm'))
# height = eval(input('enter height cm'))
#
#importing the function

# max_result = size(length,width,height)
# print(max_result)
#
# NOW TRYING TO CODE WITHOUT THE MAX FUNCTION:
# Initial attempt

# def max_num(a,b,c):
#     x = a
#     y = b
#     z = c
#     for i in (x,y,z):
#         return max()
#
# #importing the function
# length = eval(input('enter length in cm'))
# width = eval(input('enter width cm'))
# height = eval(input('enter height cm'))
#
# #we are reusing our function
# max_result = max(length,width,height)
# print(max_result)
# #
# # I have used the max function and but not without it yet

#Amended

def maxi(a,b,c):
    num = 0
    if a >=b and a>=c:
        return a
    if b >=c and b>=a:
        return b
    if c >=a and c>=b:
        return c


length = eval(input('enter length in cm'))
width = eval(input('enter width cm'))
height = eval(input('enter height cm'))

# importing function
max_result = maxi(length,width,height)
print(max_result)
