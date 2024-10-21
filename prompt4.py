#Write a Python program that declares a class describing your favorite animal. Have the data members of the class represent the following physical parameters of the animal: length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool). Write an initialization function that sets the values of the data members when an instance of the class is created. Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.

import sys

class LemonShark:
    
    #this is all the info that will get printed, calling upon the __init__ meethod to fill in the values
    def print(self):
        print("Lemon Shark!")
        print(f"Length of arms = {self.arm_length} (Lemon sharks don't have arms)")
        print(f"Length of legs = {self.leg_length} (Lemon sharks don't have legs)")
        print(f"Number of eyes = {self.eyes_num}")
        print(f"Tail? {self.has_tail}")
        print(f"Furry? {self.is_furry}")
        
    #this is the constructor method that sets up the parameters
    def __init__ (self, arms, legs, eyes, tail, furry):
        self.arm_length = arms
        self.leg_length = legs
        self.eyes_num = eyes
        self.has_tail = tail
        self.is_furry = furry

#setting up the default values
def main(): 
    arms = 0.0
    legs = 0.0
    eyes = 2
    tail = True
    furry = False
    
    #initialize and print
    lemon_shark = LemonShark(arms,legs,eyes,tail,furry)
    lemon_shark.print()
    
if __name__ == "__main__":
    main()
        
