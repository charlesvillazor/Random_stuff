#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:17:26 2018

@author: charlesvillazor
"""
#cheerbot 3.0 (improved mechanics)
vowel = "aeiouAEIOU"
space = " "
cheer = input("Type the words you want to be cheered, type in all uppercase for max excitement: ")
hype = int(input("Type your level of hype on as a number on a scale of 1-30 "))
if hype<25:
    for char in cheer:
        if char in vowel:
            print("Give me an" + " " + char + "! " + char)
        elif char in space:
            print (" ")
        else:
            print("Give me a  " + char + "! " + char)
if hype>=25:
    for char in cheer:
        if char in vowel:
            print("GIVE ME AN" + " " + char + "! " + char)
        elif char in space:
            print(" ")
        else:
            print("GIVE ME A  " + char + "! " + char)
print(" ")
value_2 = 1
if hype<25:
    print("What does that spell?")
    while value_2 <= hype:
        print(cheer+"!")
        value_2 = value_2 + 1
if hype>25:
    print("WHAT DOES THAT SPELL???")
    while value_2 <= hype:
        print(cheer+"!!!")
        value_2 = value_2 + 1