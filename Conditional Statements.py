#in Python IF is the only conditional statement.

# # IF ELSE STATEMENTS
# balance = 100
# withdraw = 120
# name = 'Muriithi'
#
# if withdraw <= balance:
#     print('Withdraw success')
# else:
#     print('Insufficient funds')
#
# balance = 100
# withdraw = 20
# name = 'Said'
#
# if withdraw <= balance and name == 'Said':
#     print('Withdraw success')
# else:
#     print('Insufficient funds or not Said')

# IF ELIF ELSE STATEMENTS'
# score = 'Excellent'
# if score == 'Excellent':
#     print ('Green Label')
# elif score == 'Good':
#     print ('Blue Label')
# elif score == 'Poor':
#     print('Red Label')
# else:
#     print('Unrecognised')

#Grade students based on average
#Task
# Ask a user to enter the following marks -  (Use input faction)
#  Math = 60
#  Eng = 60
#  Kiswahili = 60
#  SSR = 60
#  SCI = 60
# Calculate the total of the marks
# Calculate the average
#Using the average, give grades to the students (Use and IF ELIF statement
# #grading
# # 80  100 = 'A'
# # 70 - <80 = 'B'
# # 60 - <70 = 'C'
# # 50 - <60 = 'D'
# # <50 = 'E'
#
math = input ('enter math score:')
print(math)
print (type(math))

kis =  input('enter kiswahili score:')
print(kis)
#
ssr = input('enter ssr score:')
print(ssr)
#
sci = input('enter sci score:')
print(sci)
#
math1 = int(math)
kis1 = int(kis)
ssr1 = int(ssr)
sci1 = int(sci)
#
total = math1+kis1+ssr1+sci1
print(total)
#
actualtotal =  int(total)
print(actualtotal)
#
average = actualtotal/4
print(average)
#
if average >= 80 and average <= 100:
     print('A')
elif average >= 70 and average <80:
     print ('B')
elif average >= 60 and average <70:
     print ('C')
elif average >= 50 and average <60:
     print ('D')
elif average <50:
     print ('E')
else:
    print('Exam not done')

# name = input ('Enter your name:')
# print (name)



