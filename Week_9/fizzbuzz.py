#! python 3

"""
Simeon Patton
CS362 - Oregon State Spring 2021
Homework 7 - Question 1.2
fizzbuzz.py
"""

def output():
    ## Creating loop that will populate string
    for i in range (1, 100):
        ## Empty string creation to add to
        fizz_buzz = ""
    
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz = (fizz_buzz + "fizzbuzz")
        elif i % 3 == 0:
            fizz_buzz = (fizz_buzz + "fizz")
        elif i % 5 == 0:
            fizz_buzz = (fizz_buzz + "buzz")
        else:
            fizz_buzz = str(i)
        print(fizz_buzz)
    return fizz_buzz


if __name__ == '__main__':
    output()
    
