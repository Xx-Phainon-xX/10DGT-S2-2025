#Creating an input system for our coffe program
#Author: Joanna Liao
#Date: 01-10-2025


#Version 2.0
#TODO: Ask the user if they like coffee
#      Record the anser
#      Give a response back to user

#Version 1
#Ask the user whether they like coffee or not
'''Like_coffee=input("Do you like to drink coffee? ")
print(f'Your answer was "{Like_coffee}".')

if Like_coffee=="yes":
 print("That is great, I like coffee too")

else: 
    print("You are missing out! Why not give it a try?")'''

#Version 2.0
#While loop
'''keep_going = "" #The variable contains an empty string
while keep_going =="":
    like_coffee=input("Do you like to drink coffee? ")
 
    if like_coffee=="yes" or like_coffee== "Yes" or like_coffee== "y":
        print("That is great, I like coffee too")
        keep_going= "finished"
    elif like_coffee== "no" or like_coffee== "No" or like_coffee== "n": 
        print("You are missing out! Why not give it a try?")
        keep_going="finished" 
    else:
        print("I don't understand")'''
        


 #Version 3.1
 #Making program more pythonic
def coffee_program ():
     keep_going = ""
     while keep_going == "":
        #convert answer to lower cause using .lower()
        like_coffee = input("Do you like coffee? \n").lower()
        if like_coffee == "yes" or like_coffee== "y":
            print("That's great! I like coffee too")
            
        elif like_coffee == "no" or like_coffee == "n":
            print("You are missing out! Why not give it a try?")

            like_tea= input("Do you like tea instead?\n").upper()
            if like_tea == "YES" or like_tea == "Y":
                print("Good for you, you should also give coffee a try")
        
            elif like_tea == "NO" or like_tea == "N":
                print("I am sorry. That is all I have for you")

            else:
                print("I don't understand. Please answer with either yes or no")
            
        else: #error message
            print("I don't understand")

        keep_going = input ("Press <return> to continue, or any other kep to quit. Thanks!")`

if __name__== "__main__"