#Creating an input system for our coffe program
#Author: Joanna Liao
#Date: 01-10-2025


#Version 1.0
#TODO: Ask the user if they like coffee
#      Record the anser
#      Give a response back to user

#Ask the user whether they like coffee or not
Like_coffee=input("Do you like to drink coffee? ")
print(f'Your answer was "{Like_coffee}".')

if Like_coffee=="yes":
 print("That is great, I like coffee too")

else: 
    print("You are missing out! Why not give it a try?")
