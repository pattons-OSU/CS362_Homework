#! python3

from math import *
from statistics import *

def user_list():
    number_list = [9, 5, 6, 93]
    average = mean(number_list)
    ##print(average)
    ##print(number_list)
    return number_list

'''
def add_to_list(number_list):
    return{"Number list": number_list}



def user_input():
    user_input = input("\nPlease enter a number to add to the list.\n")
    user_input = list(user_input)
    return user_input

if __name__ == '__main__':
    user_input = user_input()
    print(user_list(user_input))
'''

if __name__ == '__main__':
    user_list()
    