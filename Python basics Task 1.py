#task 1 Write a program which accepts a string as input to print
# "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No".
#Hint: Use input () to get the persons input


#Initial trial answer
# name = input('What is the synonym for affarmative:')
#
# if name == 'YES':
#     print('Yes')
# elif name == 'Yes':
#     print ('Yes')
# elif name == 'yes':
#     print('Yes')
# else:
#     print('No')

#this has ran ocrrectly

#changes from teacher

# name = input('What is the synonym for affarmative:')
# if name == 'YES' or name == 'Yes' or name == 'yes':
#     print('Yes')
# else:
#     print('No')

#further changes where we use a function

def affirmative_synonym(x):
    if x == 'YES' or x == 'Yes' or x == 'yes':
        return ('Yes')
    else:
        return ('No')

name = input('What is the synonym for affarmative:')
res = affirmative_synonym(name)
print(res)
