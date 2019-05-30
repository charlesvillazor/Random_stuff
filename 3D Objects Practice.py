#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 02:03:02 2018

@author: charlesvillazor
"""
#Object oriented programming. 3D coordinates and 3D vectors.
#Edit: This turned into my general calc 3 calculator. nice.
import math
class three_coordinates(object): #Starting with 3D coordinates
    def __init__(self, x, y, z): #Initializing object, what attributes are needed.
        assert type(x) == int, "numbers must be integers!"
        assert type(y)== int, "numbers must be integers!"
        assert type(z) == int, "numbers must be integers!"
        self.x = x
        self.y = y
        self.z = z
    def __str__(self): #When printing the object, returns (x,y,z).
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"
    def distance(self, other): #Obtain distance between two points.
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        z_diff_sq = (self.z-other.y)**2
        distance = (x_diff_sq+y_diff_sq+z_diff_sq)**0.5
        return distance
    def points_to_vector(self, other):
        x_comp = (other.x-self.x)
        y_comp = (other.y-self.y)
        z_comp = (other.z-self.z)
        return three_vect(x_comp,y_comp,z_comp)
    def create_plane(self, other_1, other_2):
        '''
        This gives what is needed to make a plane equation containing three points
        in vector form. I've taken a long time to think about how to get an
        equation back.
        '''
        vector_parallel_1 = three_coordinates.points_to_vector(self,other_1)
        vector_parallel_2 = three_coordinates.points_to_vector(self,other_2)
        normal_vector = three_vect.cross_product(vector_parallel_1,vector_parallel_2)
        return str(normal_vector)+"·"+"(<x,y,z>-"+str(vector_parallel_1)+")"+"=0"
    #I don't know what else coordinates are used for.

class three_vect(object): #And now 3D Vector
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self): #print statement
        return "<"+str(self.x)+","+str(self.y)+","+str(self.z)+">"
    def __add__(self,other): #Add two vectors!
        add_x = self.x + other.x
        add_y = self.y + other.y
        add_z = self.z + other.z
        vector_sum = three_vect(add_x,add_y,add_z)
        return vector_sum
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
        vector_difference = three_vect(sub_x,sub_y,sub_z)
        return vector_difference
    def __mul__(self, float): #Multiplying vector and scalar!
        mul_x = self.x*float
        mul_y = self.y*float
        mul_z = self.z*float
        vector_product = three_vect(mul_x,mul_y,mul_z)
        return vector_product
    def dot_product(self, other): #Find the dot product of two vectors!
        dot_x = self.x * other.x
        dot_y = self.y * other.y
        dot_z = self.z * other.z
        dot_product = dot_x+dot_y+dot_z
        return dot_product
    def cross_product(self, other): #Find the cross product of two vectors!
        cross_x = (self.y*other.z)-(self.z*other.y)
        cross_y = (self.z*other.x)-(self.x*other.z)
        cross_z = (self.x*other.y)-(self.y*other.x)
        cross_product = three_vect(cross_x,cross_y,cross_z)
        return cross_product
    def angle(self, other): #Find the angle between two vectors, returns answer in radians.
        dot_product = self.dot_product(other)
        mag_self = self.magnitude()
        mag_other = other.magnitude()
        mag_both = mag_self*mag_other
        cos_angle = dot_product/mag_both
        angle = math.acos(cos_angle)
        return angle
    def scalar_projection(self, other): #Find the scalar projection of one vector onto another
        '''
        In this function, the self is the "base" of the equation Comp_a_(b).
        In other words, the other vector is projecting itself onto the self vector in one dimension
        '''
        dot_ab = three_vect.dot_product(self, other)
        magnitude = three_vect.magnitude(self)
        scalar_projection = dot_ab/magnitude
        return scalar_projection
    def vector_projection(self, other):#Find vector projection of b on to a
        '''
        Again, the self is the master vector being projected on, and the other is the
        vector that is being projected. Outputs a Vector!
        '''
        dot_ab = three_vect.dot_product(self, other)
        magnitude_squared = (three_vect.magnitude(self))*(three_vect.magnitude(self))
        scalar = float(dot_ab/magnitude_squared)
        vector_projection = three_vect(scalar*self.x, scalar*self.y, scalar*self.z)
        return vector_projection
    def orthogonal_projection(self, other):
        '''
        similar to the last three, the self is the vector being projected on, the other
        is the vector being projected
        '''
        projected_normal = three_vect.vector_projection(self, other)
        orthogonal_projection = other - projected_normal
        return orthogonal_projection
    def scalar_triple_product(self, other_1, other_2):
        '''
        This is to get the volume of a parallelopiped.
        If you don't know what that is, this gives you the discriminant of the
        linear transformation in R^3.
        other_1 and other_2 are the two components of the cross product (the bases)
        and self is the vector orthongonal to them.
        '''
        cross_product = three_vect.cross_product(other_1, other_2)
        answer = three_vect.dot_product(self, cross_product)
        return answer
    
a = three_vect(20.938,21.356,0)
b = three_vect(22.04,25.68,0)
c = three_vect(6.49,1.23,0)
print(three_vect.cross_product(a,b)*3)
print(b)
print(three_vect.angle(a,b))
print(three_vect.cross_product(c,a)*4.43)