#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:52:52 2018

@author: charlesvillazor
"""
#Project Euler Problem 1 Solution
#Find the sum of all the multiples of 3 or 5 below 1000. The answer is 233168.
def f(all_multiples): 
    #Finds the sum of all mutiples
    z = sum(all_multiples)
    return print(z)
def g(x):
    #Finds the multiples of x
    lists_of_multiples_of_x = []
    value = 0
    multiples_of_x = x*1
    while multiples_of_x < 999: #This number is the last multiple until 1000 for 3
        multiples_of_x = x*value
        value = value + 1
        lists_of_multiples_of_x.append(multiples_of_x)
    return lists_of_multiples_of_x
def h(y):
    #Finds the multiples y
    lists_of_multiples_of_y = []
    value = 0
    multiples_of_y = y * 1
    while multiples_of_y < 995: #This number is the last multiple until 1000 for 5
        multiples_of_y = y*value
        value = value + 1
        lists_of_multiples_of_y.append(multiples_of_y)
    return lists_of_multiples_of_y
def i(lists_of_multiples_of_x,lists_of_multiples_of_y):
    #Puts multiples in one list and also removes duplicates
        all_multiples = lists_of_multiples_of_x+lists_of_multiples_of_y
        return list(set(all_multiples)) #A set is a list without duplicates
def answer():
    x = 3
    y = 5
    lists_of_multiples_of_x = g(x)
    lists_of_multiples_of_y = h(y)
    all_multiples = i(lists_of_multiples_of_x,lists_of_multiples_of_y)
    f(all_multiples)
    return print("Euler can suck it")
answer()
'''
As sort of a learning experience, I've learned that the "while" operations I used to create the lists of 
multiples always goes one over the number stated not to go over. For example, when I put in 1000 for each
as a value not to go above, both went above by one more multiple. It makes sense because of how a 'while'
loop works, but it kinda sucks I had to go debugging this problem. Ah well, it was a nice exercise.
And I did it mostly alone, the only things I had to do was understand what I did wrong.
Programming is hard.
Time Spent: ~1:15:00
'''

##This is the same solution in one line. I did it in 37 lines. But like it works, so whatever.
#x = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
#print(x)
