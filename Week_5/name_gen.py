#! python3

## Simeon Patton
## CS362 HW4 Question 3.1
## April 30, 2021

## Write code that generates a full name when you provide the first and
## last name as inputs.

## Use the unittest module and write any 3 tests that can test out your
## code.

def first_name_input():
    first_name = input("\nPlease enter your first name: \n")
    return first_name
    
def last_name_input():
    last_name = input("\nPlease enter your last name: \n")
    return last_name

def full_name(first_name_input, last_name_input):
    space = " "
    full_name = first_name_input + space + last_name_input
    return full_name



if __name__ == '__main__':
    print("")
    print(full_name(first_name_input(), last_name_input()))
    print("")