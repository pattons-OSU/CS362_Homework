#! python3

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