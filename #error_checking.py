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
#Use the function parameters to make my code
#More pythonic

'''def test_int(question): #question entered is a placeholder
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
print(f"your number is {sum}")'''

#Code that tests whether a valid imput is given (v1.4)
#Use the function parameters to make my code more pythonic

def valid_num(question, low, high):
    error=f"Whoops, that is not an interger between {low} and {high}."
    while True:
        try:
            response= int(input(question))
            #if response >= 0 and response <=10
            if low<=response<=high:
                break #This stops the loop
            else: 
                print(f"{error}\n")
        except ValueError:
            (print(error))
    return response #This makes the response avaliable to be
if __name__=="__main__":
    num_1=valid_num("Enter a number between 1 and 10 ", 1, 10)
    print(f"You entered {num_1}\n")

    num_2=valid_num("Enter a number between 1 and 10 ", 600, 700)
    print(f"You entered {num_2}\n")

    num_3=valid_num("Enter a number between 67 and 76 ", 67, 76)
    print(f"You entered {num_3}\n")

    #multiplying the numbers
    multiply= num_1*num_2*num_3
    print(f"The total of {num_1}, {num_2}, and {num_3} is {multiply}.\n")

    #adding the numbers
    sum= num_1+num_2+num_3
    print(f"The total of {num_1}, {num_2}, and {num_3} is {sum}.\n")