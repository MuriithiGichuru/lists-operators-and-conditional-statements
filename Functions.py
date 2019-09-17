# A function is like a named reusable block of code used to perfom a related action
# a = 0
# b = 0
# a= a + 2
# b= b + 3
#if the above code is reusable, we then name this functions
# a = 0 # define
# b = [] #list
# c = {} # dictionary
# d = () #upple

# # to create / defining a new function, we use def
# # def is the key word that python uses to create a new function
# #'add_two_numbers' is the name of our function
# # a and b are the PARAMETERS of our function
# # c is the reurn value
#
# def add_two_numbers(a,b):
#     c = a + b
#     return (c)
#
# #importing the function
# from functions import add_two_numbers
# first_number = eval(input('enter first number'))
# second_number = eval(input('enter second number'))
# #we are reusing our function
# result = add_two_numbers(first_number,second_number)
# print(result)
#
#
#
# #concatinates
# def add_two_names(first_Name, last_name):
#     full_name = first_Name + last_name
#     return (full_name)
#
# res = add_two_names('Muriithi',' Gichuru')
# print(res)
#
# student1 = [12,23,34,45,65]
# student2 = [22,23,34,45,65]
# student3 = [32,23,34,45,65]
# student4 = [42,23,34,45,65]
#
# # total1 = student1[0]+ student1[1] + student1[2] + student1[3]+ student1[4]
# # total2 = student2[0]+ student2[1] + student2[2] + student2[3]+ student2[4]
# # total3 = student3[0]+ student3[1] + student3[2] + student3[3]+ student3[4]
# # total4 = student4[0]+ student4[1] + student4[2] + student4[3]+ student4[4]
#
# def total(math,eng,kis,ssr,sci):
#     alama = math + eng + kis + ssr + sci
#     return(alama)
# # alama is only known within this function
#
#
#
# def average(math,eng,kis,ssr,sci):
#     average = (math + eng + kis + ssr + sci) / 5
#     return (average)
#
# # average1 = total1/5
# # average2 = total2/5
# # average3 = total3/5
# # average4 = total4/5
#
# from functions import total
# from functions import average
#
# marks = total(12,23,34,45,65)
# result1 = alama
# print (result1)
#
# ave = average(marks/4)

#write a function called sum_digits that is given an integer num and returns the sum of the digits of num


    #hint use a for loop
    #convert num to string and then add and then conver it back to integer
def sum_digits(num):
    sum_of_digits = 0 # using a 0 identifes this as an integer starting from 0
    num = str(num) # we convert the integer into a string so that we can look at ever element within it
    for i in num:
        sum_of_digits = sum_of_digits + int(i) #this line says that from str element 0. i is a string and we should conver it into an integer (which is int(i)) is a string so we need to convert it back to an integer to allow
    return sum_of_digits

res = sum_digits(353535)
print(res)

