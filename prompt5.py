#Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2 with a thousand entries. Follow the basic Python program structure, including a main program function.

import numpy as np
from astropy.table import Table

x_values = np.linspace(0, 2, 1000) #this creates 1000 points from 0 to 2
sin_values = np.sin(x_values) #the sin values of all the x values


def mr_table():
    data = Table([x_values,sin_values],names=['x','sin(x)'])
    print(data)

def main():
    mr_table()
    
if __name__ == "__main__":
    main()
