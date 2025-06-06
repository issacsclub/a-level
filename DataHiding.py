# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 15:44:36 2025

@author: Support
"""

class employee:
    
    def __init__(self,name, staffNo):
        self.__name = name #
        self.__staffNo = staffNo #public
        
        
    def showDetails(self):
        print("Employee Name: ", self.__name)
        print("Employee Number: ", self.__staffNo)
        
myStaff = employee("Eric Jones", 7878)
#myStaff.showDetails()
