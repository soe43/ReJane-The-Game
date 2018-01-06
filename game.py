#Name: William Soe
#ReJane: The Game
#Ms. Thoms British Literature
#Period 7

#To sleep running statements
import time
import random
import sys

name = ""

def intro():
    print("ReJane: The Game")
    print("A game developed by William Soe")
    print ("Ms. Thoms's British Literature Class Period 7\n")
    sys.stdout.flush()
    
def naming():
    sys.stdout.flush()
    name = ""
    name = raw_input('What would you like your name to be? ')
    sys.stdout.flush()
    print("Hello " + name + "! Let's begin.")
    sys.stdout.flush()
    return name


intro()
name = naming()
          
    
    
