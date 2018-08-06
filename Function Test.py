#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:18:07 2018

@author: charlesvillazor
"""
#Program to test functions, uses two past scripts. I never want to do this again.
def log_call():
    low = 0
    attempts = 1
    print("This program can compute logs given the base. Please enjoy")
    log = float(input("Input the log number here, keep it under 200: "))
    high = log
    base = float(input("Input the base of the log here: "))
    alpha = float(input("Input the decimal accuracy you want here, from 0-1. Smaller decimals will be more accurate but slower: "))
    guess = (high+low)/2.0
    while abs((base**guess) - log) >= alpha:
        if base**guess > log:
            high = guess
        else:
            low = guess
        guess = (high+low)/2.0
        attempts = attempts+1
    print("The log of your number is", guess, "the the accuracy of", alpha)
    return print("This calculation took", attempts, "attempts")
def cube_root_call():
    low = 0 
    attempts = 0
    print("This program will give the cube root of a number")
    cube = int(input("Put your number that you want cube rooted here: "))
    alpha = float(input("Now put in the degree of accuracy you would like, from 0-1. Smaller decimals are more accurate, but take longer, and vice-versa: ")) #alpha, the degree of accuracy of this program.
    high=cube 
    guess = (high+low)/2.0 
    while abs(guess**3 - cube) >= alpha:
        if guess**3 < cube:
            low = guess
        else:
            high= guess
        guess = (high+low)/2.0 
        attempts = attempts+1 
    print("The cube root of the number is:", guess, "to the accuracy of", alpha)
    return print("This calculation took", attempts, "attempts.")
print("Please type 'log' or 'cube root' to find the log of a number or the cube root of a number")
value = str(input("Input 'cube root' or 'log' here: "))
if value == "log":
    print(log_call())
elif value == "cube root":
    print(cube_root_call())
else:
    print("For not following the rules, you get nothing.")
'''
Functions were really something else to make but I'm pretty proud I got this rather simple function to work.
This entire thing is 50 lines long, which is the longest code I've made to this date. Maybe I'll compile all
of the formulas I've ever made into one script. Kidding, that would kill me to make. What was most interesting
about this is that the programs didn't even need the variables that are used in the name to make. Functions
that just used to output numbers instead of also input them (like my scripts did) need inputs. Useful to
remember
'''