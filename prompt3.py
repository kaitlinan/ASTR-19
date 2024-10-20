#Write a Python program that defines a function f(x) that returns x**3 + 8. In the main function of the program, call f(x) with x = 9 and print the result.  Use an if statement that executes if the result is larger than 27 and prints “YAY!”.

import numpy as np
import sys

def f(x): #this defines the f(x) function and returns the resulting number when its called to print in the main function
    return(x**3 + 8)

def main():
    
    x = 9  #defines x as 9 and prints f(9) as a float
    print(f(float(x)))
        
    
    if (f(x)>27):  #if f(9) is greater than 27, YAY! gets printed
        print('YAY!')
            
    
if __name__=="__main__":
    main()
    