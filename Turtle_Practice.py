#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:27:52 2019

@author: charlesvillazor
"""
import turtle as draw
window = draw.Screen() #this object is a screen for which the turtle moves
window.bgcolor("lightblue") #changes the background of the window color
evelyn = draw.Turtle() #this function creates a turtle at (0,0)
evelyn.color("green")
##def square_spiral():
##    displacement = 10 #displacement is the distance the turtle travels
##    for i in range(50): #repeats given fuction some amount of times
##        evelyn.fd(displacement) #this moves the turtle some amount forward
##        evelyn.lt(90) #turns turtle some degree to the left
##        displacement= displacement+10
##    return window.bye()

##def semicircle(): #creates a semicircle
##    evelyn.circle(100,180)
##    evelyn.lt(90)
##    evelyn.fd(200)
##    return window.bye()

def spiral(): #This spiral is much more refined than the square one. 
    displacement = 1.0 #displacement is the distance the turtle travels
    for i in range(1000): #repeats given fuction some amount of times
        evelyn.fd(displacement) #this moves the turtle some amount forward
        evelyn.lt(15) #turns turtle some degree to the left
        displacement= displacement+0.09
    return window.bye()
spiral()
