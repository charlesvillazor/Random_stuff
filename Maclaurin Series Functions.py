#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:54:56 2018

@author: charlesvillazor
"""
def fact(x):
    if x == 0:
        return 1
    else:
        return x*fact(x-1)
    
def exponential_series(x):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    answer = 0
    n=0
    while n != 500: #the accuracy of 500 terms
        answer = (x**n)/(factorial(n)) + answer
        n = n+1
    return answer

def sin(x): #in radians. Just convert degrees to radians.
   def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
   n=0
   answer = 0
   while n!= 500: #again, 500 terms
       answer = (((-1)**n)*(x**((2*n)+1)))/factorial(((2*n)+1)) + answer
       n = (n+1)
   return answer

def cos(x): #radians
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    n=0
    answer = 0
    while n!= 500: #again, 500 terms
       answer = (((-1)**n)*(x**(2*n)))/factorial(2*n) + answer
       n = (n+1)
    return answer

def inverse_tan(x): #radians, only do numbers -1<x<1. I'm not exactly sure why, but that goes into math rather than computer science.
    n=0
    answer=0
    while n!=500:
        answer = (((-1)**(n))*(x**((2*n)+1)))/((2*n)+1) + answer
        n=n+1
    return answer

def deg_to_rad(degrees): #convert anything above 360 degrees to something below that. 
    radians = degrees*(3.141592653589793238/180)
    return radians
