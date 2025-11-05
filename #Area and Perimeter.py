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
    return response

print("Welcome to my area and perimeter calculator")
name=input("What is your name? ")

# Main Routine starts here
keep_going = ""
while keep_going == "" :

      #get width and height
  width= num_check(f"{name}, please enter the width of the shape:")
  height=num_check(f"{name}, please enter the height of the shape:")

#Calculate the area/ perimeter
  area = width * height
  perimeter = 2 * (width + height)

#Output the area and perimeter
  print()
  print(f" The perimeter of your shape is: {perimeter} square units")
  print(f" The area of your shape is: {area} square units")
  keep_going=(input("Please press enter if you wish to continue or any key to quit"))

      