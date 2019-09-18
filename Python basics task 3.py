#TASK 3:
#Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and
# last elements of the given list. For practice,
# write this code inside a function


#First part done as a list

# a = [5, 10, 15, 20, 25]
# print ("The original list is : " +  str(a))
# res = [ a[0], a[-1]]
# print ("The first and last element of list are : " +  str(res))

# #Done as a function
def first_last_element(x):
    return (x[0], x[-1])

a = [5, 10, 15, 20, 25]
res = first_last_element(a)
print(res)


#This has run correctly
#result is a tupple not a list / string



