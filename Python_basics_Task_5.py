# TASK 5:
# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
# write a program to print the first half values in one line
# and the last half values in one line.

# def slice_tup(x):
#     for i in range (0 , len(0.5*x)):
#         return((x), end=' ')
#     for i in range (len(0.5*x),len(x)):
#         return((0.5*x), end= ' ')
#
#  tup = (1,2,3,4,5,6,7,8,9,10)
#  tup1 = slice_tup(tup)
#  print(tup1)

# #my example
# tup = (1,2,3,4,5,6,7,8,9,10)
# list1 =[]
# list2 = []
# for i in range(0,5):
#     list1.append(tup[i])
# for i in range(5,10):
#     list2.append(tup[i])
# print(list1)
# print(list2)
#
#
# # this has run correctly
# # #split the two lists into 2 different lines
# #
#
#
# #example 2
# tup = (1,2,3,4,5,6,7,8,9,10)
# list1 =[]
# list2 = []
# for i in range(0,len(0.5*tup)):
#     list1.append(tup[i])
# for i in range(5,10):
#     list2.append(tup[i])
# print(list1)
# print(list2)

#example 3 -from the teacher
tup1 = (1,2,3,4,5,6)
divider = int(len(tup1)/2) # without the int, the calculation results in a float. so we typecast
tp1 = tup1[:divider]
tp2 = tup1[divider:]
print(tp1)
print(tp2)