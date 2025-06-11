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
    def __init__(self, radius):
      shape.__init__(self)
      self.__radius = radius
    def area (self):
      self.__areaValue = self.__radius * self.__radius * 3.142
      print("Area ", self.__areaValue)
myCircle = circle(20)
myCircle.area()
myRectangle = rectangle (10,17)
myRectangle.area()