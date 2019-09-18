#

# def print_hello(n):
#     print('Hello!'* n)
#     print()
#
# print_hello(3)
# print_hello(5)
# times = 2
# print_hello(times)

# def convert(t):
#     return t*9/5+32
# print (convert(2))

 #TASK 2:
# Implement a function that takes as input three variables,
# and returns the largest of the three.
# Do this without using the Python max () function!
# The goal of this exercise is to think about some internals
# that Python normally takes care of for us


# def size (a,b,c):
#     return max(a,b,c)
#
# #importing the function
#
# length = eval(input('enter length in cm'))
# width = eval(input('enter width cm'))
# height = eval(input('enter height cm'))
#
# #we are reusing our function
# max_result = size(length,width,height)
# print(max_result)

def max(a,b,c):
    x = [] = a[0]
    for i in a:
        if res < i:
            res = 1
    return res



#importing the function
length = eval(input('enter length in cm'))
width = eval(input('enter width cm'))
height = eval(input('enter height cm'))

#we are reusing our function
max_result = max(length,width,height)
print(max_result)

# we have used the max function and but not without it yet