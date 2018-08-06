#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:15:08 2018

@author: charlesvillazor
"""
#Newton's law of gravitation program
G=6.67408*(10**(-11))
print("this calculates gravitational force between two objects")
print("input the mass of object one now, be sure it is in kilograms")
m1 = float(input(" "))
print("now input the mass of obeject two, in kilograms as well")
m2 = float(input(" "))
print("now input the distance between the two objects, in meters")
r = float(input(" "))
print("the force between the two objects is", (G*m1*m2)/(r**2), ("newtons") )
#Well at this point I should have a good grasp of how inputs work, as this is my third one I made. It's also seemingly the most complicated one.