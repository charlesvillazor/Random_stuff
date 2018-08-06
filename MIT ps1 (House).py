#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:16:19 2018

@author: charlesvillazor
"""
#program for MIT second problem, assignment 1
portion_down_payment = 0.25 
r = 0.04
print("you will now try and put a down payment on a house") 
print("please input your annual salary, it is needed to put a down payment for the house") 
annual_salary = float(input("input annual salary here: ")) 
portion_saved = float(input("now input the portion of your annual pay that you want to be saved for this down payment. write this as a decimal: "))
semi_annual_raise_rate = float(input("now input the decimal of semi annual raise you would get after 6 months: "))
total_cost = float(input("now input the total cost of your dream house: ")) 
monthly_salary = (annual_salary/12) 
month = 0 
value = 1
current_savings = 0 
while current_savings<(total_cost*portion_down_payment):
    month = month+1 
    current_savings = current_savings+(current_savings*r/12)+(monthly_salary*portion_saved) 
    if month == value*6:
        monthly_salary = monthly_salary+(monthly_salary*semi_annual_raise_rate)
        value=value+1
'''
the only change in this program from the first problem is the semi annual raise rate function. this is done by
adding an "if" condition, with a variable "value" controlling when it happens
'''
print("the amount of months you will need to save up for your house is", month) 
print("the amount of years it will take is ", (month/12))