# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 12:03:47 2025

@author: Support
"""

class shape:
    def __init__(self):
      self.__areaValue = 0
      self.__perimeterValue = 0
    def area(self):
      print("Area ", self.__areaValue)
    def perimeter(self):
      print("Perimeter ", self.__areaValue)
      

        
class rectangle(shape):
    def __init__(self, length, breadth):
      shape.__init__(self)
      self.__length = length
      self.__breadth = breadth
    def area (self):
      self.__areaValue = self.__length * self.__breadth
      print("Area ", self.__areaValue)
class circle(shape):
    def __init__(self, radius, pi=3.14): # overloading, circle can be called with/without pi
      shape.__init__(self)
      self.__radius = radius
      self.pi = pi
    def area (self):
      self.__areaValue = self.__radius * self.__radius *self.pi
      print("Area ", self.__areaValue)
      
class Square(shape):
    def __init__(self, length):
      shape.__init__(self)
      self.__length = length
     
    def area (self):
      self.__areaValue = self.__length * self.__length
      print("Area ", self.__areaValue)
      
myCircle = circle(20,22/7)
myCircle.area()

myRectangle = rectangle (10,17)
myRectangle.area()

mySquare = Square (10)
mySquare.area()

