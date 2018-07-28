# May Pena
# Generates rectangles with a random widths
# and heights, and colors on the screen.
# This is a rough imitation of Piet Mondrian art. 

from random import *
from graphics import *

def main():
    win = GraphWin("Lab 7", 600,600)
    for i in range(10000):
        
        x1 = randint(0,600)
        y1 = randint(0,600)
        x2 = randint(0,600)
        y2 = randint(0,600)
        red   = randint(0,255)    
        green = randint(0,255)     
        blue  = randint(0,255)   
        color = color_rgb( red, green, blue )
   
        r = Rectangle( Point(x1,y1), Point(x2, y2) )
        r.setFill( color )
        r.draw( win )
    
main()
