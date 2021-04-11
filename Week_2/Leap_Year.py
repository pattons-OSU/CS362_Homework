## Simeon Patton
## CS362 HW1 Question 4
## April 10, 2021

## Simple python program to determine if a users inputted year is a leap year.

## Idea behind modulus  coding inspored by ourcodeworld.com "How to determine 
## whether a year is a leap year or not in programming",  found at www.shorturl.at/pDJU1


## Import os to get the size of the display
import os
display_size = os.get_terminal_size()

## Printing display break * size of user display
print("")
print("-" * display_size[0])


print("")
in_year = input('Please enter the year that you would like to check: ')
in_year = int(in_year)
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