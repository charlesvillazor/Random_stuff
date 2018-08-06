#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 02:03:02 2018

@author: charlesvillazor
"""
#Object oriented programming test. 3D coordinates and 2D vectors.
import math
class three_coordinates(object): #Starting with 3D coordinates
    def __init__(self, x, y, z): #Initializing object, what attributes are needed.
        assert type(x) == int, "numbers must be integers!"
        assert type(y)==int, "numbers must be integers!"
        assert type(z) == int, "numbers must be integers!"
        self.x = x
        self.y = y
        self.z = z
    def __str__(self): #When printing the object, returns <x,y,z>.
        return "<"+str(self.x)+","+str(self.y)+","+str(self.z)+">"
    def distance(self, other): #Obtain distance between two points.
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        z_diff_sq = (self.z-other.y)**2
        distance = (x_diff_sq+y_diff_sq+z_diff_sq)**0.5
        return distance
    #I don't know what else coordinates are used for, sue me.

class three_vect(object): #And now 3D Vector
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self): #print statement
        return "["+str(self.x)+","+str(self.y)+","+str(self.z)+"]"
    def __add__(self,other): #Add two vectors!
        add_x = self.x + other.x
        add_y = self.y + other.y
        add_z = self.z + other.z
        return "["+str(add_x)+","+str(add_y)+","+str(add_z)+"]"
    def magnitude(self): #Find the magnitude of the vector, make sure to add the parantheses at the end!
        magnitude_x = self.x**2
        magnitude_y = self.y**2
        magnitude_z = self.z**2
        magnitude = (magnitude_x+magnitude_y+magnitude_z)**0.5
        return magnitude
    def __sub__(self, other): #Subtracting two vectors
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        sub_z = self.z - other.z
        return "["+str(sub_x)+","+str(sub_y)+","+str(sub_z)+"]"
    def __mul__(self, float): #Multiplying vector and scalar!
        mul_x = self.x*float
        mul_y = self.y*float
        mul_z = self.z*float
        return "["+str(mul_x)+","+str(mul_y)+","+str(mul_z)+"]"
    def dot_product(self, other): #find the dot product of two vectors!
        dot_x = self.x * other.x
        dot_y = self.y * other.y
        dot_z = self.z * other.z
        dot_product = dot_x+dot_y+dot_z
        return dot_product
    def cross_product(self, other): #Find the cross product of two vectors!
        cross_x = (self.y*other.z)-(self.z*other.y)
        cross_y = (self.z*other.x)-(self.x*other.z)
        cross_z = (self.x*other.y)-(self.y*other.x)
        return "["+str(cross_x)+","+str(cross_y)+","+str(cross_z)+"]"
    def angle(self, other): #Find the angle between two vectors, returns answer in radians.
        dot_product = self.dot_product(other)
        mag_self = self.magnitude()
        mag_other = other.magnitude()
        mag_both = mag_self*mag_other
        cos_angle = dot_product/mag_both
        angle = math.acos(cos_angle)
        return angle

origin = three_vect(1,0,0)
a = three_vect(34,25,14)
print(a.angle(origin))





































   























