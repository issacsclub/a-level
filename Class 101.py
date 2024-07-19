# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:48:06 2024

@author: Support
"""

class employee:
     def __init__ (self, name, staffno):
         self.name = name
         self.__staffno = staffno # Private attribute 
     def showDetails(self):
        print("Employee Name " + self.name)
        print("Employee Number " , self.__staffno)
myStaff = employee("Eric Jones", 72)
myStaff.showDetails()