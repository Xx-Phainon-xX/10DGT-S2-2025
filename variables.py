# demonstrate how variables are created and how they work.
# Author: Joanna Liao
# 19-07-2025
#Version 1.0

# different types of variables
# Store a string
greeting = "Hello World!"
print(greeting)

#Store a number
my_number=80 # assigned 80 to variable called my_number
print(my_number)

My_number2=7 
print(My_number2) # Don't assign values to variables that don't make sense

'''Do calculations with variables and store the result in another variable, I can now press enter as many times as I want'''

# Creating new variables
num_1= 5
num_2= 18
sum1= 5+18 #This is not good practice

sum1= num_1+num_2
print(sum1) # It is better practice doing this way

sum_string1="18"
sum_string2="5"
print(sum_string1+sum_string2)
# Turning these into strings combine the two numbers to make 185 rather than giving you the sum

print(f'My calculation for {num_1} and {num_2} is {sum1}')