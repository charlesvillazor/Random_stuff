#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:09:42 2018

@author: charlesvillazor
"""
#First python program, simple user input and output
print("input X, an integer")
'''
This is used to indicate to the user what to input
'''
user_input_x = int(input(" "))
'''
Lets the user input an integer, and also lets the computer know that an integer is being used
'''
print("now input y, an integer")
'''
Similar to above, user is being told to input y and that it should be an integer
'''
user_input_y = int(input (" "))
'''
Used to let the user input a number
'''
print("x to the power of y =", user_input_x**user_input_y)
'''
calculates and prints the answer
'''
print("x divided by y =", (user_input_x)/(user_input_y))