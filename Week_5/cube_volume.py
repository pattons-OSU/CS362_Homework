#! python3

import math

def cube_volume_calc(side_length):
    if side_length < 0:
        raise ValueError("A side cannot have a negative value.")
    return pow(side_length, 3)

def user_input():
    user_input = input("\nPlease enter a side length of a cube.\n")
    user_input = int(user_input)
    return user_input

if __name__ == '__main__':
    user_input = user_input()
    print(f"The volume of a cube with side length of {user_input} is {cube_volume_calc(user_input)}.\n")

