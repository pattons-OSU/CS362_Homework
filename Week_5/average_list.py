#! python3

## Simeon Patton
## CS362 HW4 Question 2.1
## April 30, 2021

## Write code to calculate the average of elements in a list.
## Use the unittest module and write any 3 tests that can test out your
## code.

from math import *
from statistics import *

def user_list():
    number_list = [9, 5, 6, 93]    
    return number_list

def average_of_list(number_list):
    average = mean(number_list)
    return average


if __name__ == '__main__':
    ##user_list()
    number_list = user_list()
    print(average_of_list(number_list))