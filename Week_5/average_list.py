#! python3

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