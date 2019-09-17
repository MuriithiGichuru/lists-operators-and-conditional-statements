

#we use while loops when we DONT have a defined end of a loop.
#a for loop is used when we have an end. It repeates until maximum is reached.
# #A for loop will ask when to stop running the program

# #adding something to each element in a list
# for a in range(10,101):
#     print (a)
# #adding a to each fruit in the list
# fruits  = ['mango','apples','pears','bananas','pineapple','guava','strawberry']
# for each in fruits:
#     each = each + 'a'
#     print (each)

#assignment - a list of numbers. find sum of 0-9
sum = 0
# count  = 0
# for each in range(10):
#     print('sum' + str(count) + 'time',sum)
#     sum = each + sum
#     count = count + 1
#     print(sum)
#
# # print('Muriithi Gichuru '*100)
# for each in range (2):
#     print ('Muriithi Gichuru')
#
# name =  'Muriithi Gichuru'


# name =  'Muriithi Gichuru'
# count = 1
# for each in range (1,101):
#     print(str(count)+' '+ name)
#     count = count + 1


# for each in range (1,21):
#     eachSquare = each**2
#     print(each, '---', eachSquare)
#
#
# for each in range(3):
#     num = eval(input('Enter a number: '))
#     print('The square of your number is', num*num)
# print('The loop is now complete')

# print('A')
# print('B')
# for i in range(5):
#     print('C')
# for i in range(5):
#     print('D')
# print('E')
#
# for i in range(100):
#     print(i)

# for a in range(10): # ranges from 0-9
#     print(a)
# for b in range (1,10): # this limits the range from 1-9
#     print(b)
# for c in range (3,7): # this limits the range from 3-6
#     print(c)
# for d in range (2,15,3): # this lints the range from 2-14, but also in increments of 3
#     print (d)
# for e in range(9,2,-1): # this limits the range from 9 to 3, but counts back words
#     print(e)
# for i in range(5,0,-1):
#     print(i, end = ' ')
# print('Blast off !!')
# for i in range (4):
#     print('*'*(i+1))
# # assignment
# Q1 -  write a program that prints your name 100 times vertically and horizantally
# for i in range(1,101):
#     print('Muriithi Gichuru',end =' ') # This one needs to be reviewed
#
# Q2 write a program that prints your name 100 times
# for i in range (0,100):
#     print(i+1,' Muriithi Gichuru') # this ine run correctly
#
# Q4 list of integers from 1-20 with their squares
# for i in range(1,21):
#     print(i, i*i) # this one ran correctly one method
#
# Q5, for loops to print the 8,11,14,....,89 in one line
# for i in range(8,90,3):
#     print(i, end=' ') # this one ran correctly
#
# Q6, prints numbers from 100,98,96.....,4,2
# for i in range(100,2,-2):
#     print(i,end=' ') # this one ran correctly
#
# Q7, print 10A's, 7B's 4CD's 1E,5F's 1G using 4 for loops
# for i in range(10):
#     print('A',end='')
# for i in range(7):
#     print ('B',end='')
# for i in range(4):
#     print('C',end='')
#     print('D',end='')
# print('E',end='')
# for i in range(5):
#     print('F',end='')
# print('G',end='') # This code has ran correctly
#
# Q8 - program rgar asks users name and how many times to print it
# for i in range(3):
#     print(input('Enter your name'))
# print('name entry complete')# This one has ran correctly

# Q9 - The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
# number thereafter is the sum of the two preceding numbers. Write a program that asks the
# # user how many Fibonacci numbers to print and then prints that many.

# def recur_fibo(n)
# if n <= 1:
#     return n
# else:
#     return(recur_fibo(n-1) + recur_fibo(n-2))
# nterms = int(input('how many times'))
# for i in range (nterms):
#     print(recur_fibo(i))  # further work is needed

#Q10 - Use a for loop to print a box like the one below. Allow the user to specify how wide and how
# high the box should be. [Hint: print('*'*10) prints ten asterisks.]
#
# wide = int(input('How wide'))
# tall = int(input('How tall'))
# for i in range (tall):
#     print('*'*wide)
# print('Star pattern') # this one has ran correctly. You can interchange tall and wide on the range and multiplication and it will work

# #Q11. Use a for loop to print a box like the one below. Allow the user to specify how wide and how
# #high the box should be.
# wide = int(input('How wide'))
# tall = int(input('How tall'))
# for i in range (tall):
#     print('*        *'*wide)
# print('Star pattern') # further work needed


#Q12 Use a for loop to print a triangle like the one below. Allow the user to specify how high the
#triangle should be.
#
# tall = int(input('How tall'))
# for i in range (tall):
#     print('*'*(i+1)) # This has ran correctly



#13. Use a for loop to print an upside down triangle like the one below. Allow the user to specify
#how high the triangle should be.
#
# tall = int(input('How tall'))
# for i in range (tall,0,-1):
#     print('*'*i) # this one has ran correctly


#Q14. Use for loops to print a diamond like the one below. Allow the user to specify how high the
# #diamond should be.
# tall = int(input('How tall'))
# for i in range (tall):
#     print(' '*(tall-1), '*'*(i*2+1))
# for i in range(tall,-1,-1):
#     print(' '*(tall-1),'*'*(i*2+1))



