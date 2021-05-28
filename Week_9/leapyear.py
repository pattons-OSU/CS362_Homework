#! python 3

"""
Simeon Patton
CS362 - Oregon State Spring 2021
Homework 7 - Question 2.2
leapyear.py
"""


def user_input():
    print("")
    in_year = input('Please enter the year that you would like to check: ')
    in_year = int(in_year)
    print("")
    return in_year


def year_check(in_year):
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
    ## Return true here to verify that function is running
    return True

if __name__ == "__main__":
    in_year = user_input()
    year_check(in_year)