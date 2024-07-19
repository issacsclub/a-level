# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:08:34 2024

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
    def __del___(self):
         print("Shape deleted ")
         
    # destructor

        
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




