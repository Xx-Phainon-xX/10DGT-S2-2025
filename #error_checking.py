#error_checking
#Author: Joanna Liao
#Date: 22/10/2025
#Version 1.0

#Code that tests whether a valid imput is given

'''done = False #Boolean variable set to false
while not done: 
    num = int(input("Please enter your value:"))
    done = True

print(f'"The number that you enetered is {num}."')'''

#Code that tests whether a valid imput is given
#Use the try and except method to catch errors
'''done = False
while not done:
    try: #This method tries for a valid input
        num = int(input("Please enter a number:"))
        done = True

    except ValueError:
        print("That is not a valid float number.\n")
       
print(f'"The number that you entered is {num}."')'''

#Code that tests whether a valid imput is given (v1.2)
#Create a function to call everytime I ask the user
#For a number. A function is a chunk of code that does something.
#functions can be used over and over again
#Parenthesis at the end
#To create a function, start with the word def
'''def test_int_num():
    done = False
    while not done:
        try:
            num = int(input("Please enter a number (interger): "))
            done = True

        except ValueError:
            print("This is not a valid float number. \n")

    print(f"The number that you entered is {num}.")

#Main routine
test_int_num() #This calls the function so that we can use it'''

#Code that tests whether a valid input is given (V1.3)
#Use the function perimetres to make my code
#More pythonic

def test_int(question): #question entered is a placeholder
    done = False
    while not done:
        error="That is not a valid number"
        print(question)
        try:
            num = int(input())
            done = True
        except ValueError:
            print(error)
    return(num) #Gives back the value of num so that I can use it outside of the box

#main routine
num1 = test_int("Please enter your first number:")
print (f"The first number you entered is {num1}.")

num2= test_int("Please enter your second number:")
print (f"The second number that you printed is {num2}")

sum = num1 + num2
print(f"your number is {sum}")
