#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:31:02 2018

@author: charlesvillazor
"""
#Project Euler Problem 2, Fibinocci numbers
#Find the sum of all even numbers in the Fibinocci sequence below 4 million.
def fib(x):
    '''
    Sequence to generate fibinocci numbers. Input x is the amount of terms wanted.
    Output is the fibinocci number at that term.
    This version of the fibinocci sequence is pretty slow, and only goes up to 35 terms before breaking.
    '''
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        x=fib(x-1)+fib(x-2)
    return x

def fib_list():
    def fib(x):
        '''
        Sequence to generate fibinocci numbers. Input x is the amount of terms wanted.
        Output is the fibinocci number at that term
        '''
        if x == 0:
            return 1
        elif x == 1:
            return 1
        else:
            y=fib(x-1)+fib(x-2)
        return y
    fib_list = []
    x = 0
    y = 0
    while x < 33: #amount of terms below 4 million. It's not cheating cause I accidentally found this term.
        y = fib(x)
        x = x+1
        fib_list.append(y)
    return fib_list

def only_even(value):
    '''
    Value input is a list. Takes just even values of the list.
    '''
    only_even = [x for x in value if x%2==0]
    return only_even

value = fib_list()
print(sum(only_even(value)))

'''
I got this answer correct on the first try (somehow). I'm getting a little more used to using python for 
mathematical things. It feels great too. I had to basically debug this myself so it was all the more satisfying
Also learned what the fibinocci sequence is and list comprehension. I'm getting there in the python world.
Only took 41 lines. There are probably people who have done this in less, but I'm happy about it.
...it also took about 3 hours.
'''