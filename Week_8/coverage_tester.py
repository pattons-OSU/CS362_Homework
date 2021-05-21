def stateCoverage(x,y):
    
    if(x < y):
        if(x*3 >= y*2):
            print("false1")
    if(x > y*y):
        print("false2")
    if(x*2 < y):
        print("false3")

    print("true")

def x_input():
    x = input("enter an x value:")
    x = int(x)
    return x

def y_input():
    y = input("enter a y value:")
    y = int(y)
    return y

if __name__ == "__main__":
    
    stateCoverage(x_input(), y_input())