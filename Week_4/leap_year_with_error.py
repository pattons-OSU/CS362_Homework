## Simeon Patton
## CS362 HW3 Question 3
## April 23, 2021

## Simple python program to determine if a users inputted year is a leap year.
##    ---This Python file can be run using version 3.9.0 on a Windows 10 computer.---
##            In order to run the file;
##                -Place the file within the folder that you would like
##                -Open a command Prompt and navigate to the folder that the file is stored in
##                -Type "python leap_year_no_error.py"
##                -Follow on screen prompts for user input.


## Idea behind modulus  coding inspored by ourcodeworld.com "How to determine 
## whether a year is a leap year or not in programming",  found at www.shorturl.at/pDJU1

##Error handling is in the form of a ValueError handling found on line 31. This checks to make sure
##that the user inputs a year in the valid format.



## Import os to get the size of the display
import os
display_size = os.get_terminal_size()

## Printing display break * size of user display
print("")
print("-" * display_size[0])


print("")
while True:
    try:
        in_year = input('Please enter the year that you would like to check: ')
        in_year = int(in_year)
        break
    except ValueError:
        print("")
        print(f"'{in_year}' is not a valid year, please enter a year as an integer.")
        print("")
print("")

## A leap year is a year that is divisible (with no remainder) by 4 (mod 4)
## If the year is evenly divisible by 100 it is not, unless it is simultaneously
## divisible by 400 with no remainder.
if (in_year % 4) == 0:
    if(in_year % 100) == 0:
        if(in_year % 400) == 0:
            print(in_year, "is a leap year.")
        else:
            print(in_year, "is not a leap year.")
    else:
        print(in_year, "is a leap year.")
else:
    print(in_year, "is not a leap year.")


print("")
print("-" * display_size[0])
print("")