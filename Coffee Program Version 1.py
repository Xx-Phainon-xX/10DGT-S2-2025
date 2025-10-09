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
keep_going = ""
while keep_going =="":
    like_coffee=input("Do you like to drink coffee? ")
 
    if like_coffee=="yes" or like_coffee== "Yes" or like_coffee== "y":
        print("That is great, I like coffee too")

    elif like_coffee== "no" or like_coffee== "No" or like_coffee== "n": 
        print("You are missing out! Why not give it a try?")

    else:
        print("I don't understand")
 