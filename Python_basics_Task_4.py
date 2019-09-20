# TASK 4:
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message


t = eval(input('Enter any number'))
if t%2 == 0:
    print('This is an even number ')
    if t%4 == 0:
        print('It is also divisible by 4')
else:
    print('This is an odd number')

# this has ran correctly

