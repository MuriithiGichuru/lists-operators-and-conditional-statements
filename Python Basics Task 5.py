# TASK 5:
# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
# write a program to print the first half values in one line
# and the last half values in one line.

tup = (1,2,3,4,5,6,7,8,9,10)
list1 =[]
for i in range(0,len(tup),5):
    list1.append((tup[i:i+5]))
print(list1)

# this has run correctly
#split the two lists into 2 different lines