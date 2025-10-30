#Area and Perimeter
#Author: Joanna Liao
#Date: 29-10-2025
#Version 1.0

#Ask the user for the width and height
#Assume they put in valid data

#Enter a number that is more than 0
def num_check(question):
    error= f"Please eneter a value that is more the 0 \n"
    while True:
       try:
            response=float(input(question))
            if response>0:
               break
            else:
                print(error)
       except: ValueError
       (print(error))
           
    

# Main Routine starts here
keep_going = ""
while keep_going == "" :

    #Get width and length
    for item in range (0,100000000):
        width = num_check("width:")
        print(width)

        print ()

    for item in range (0,100000000):
        height = num_check("height:")
        print(height)
        