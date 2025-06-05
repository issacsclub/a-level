# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 15:44:36 2025

@author: Support
"""

class employee:
    
    def __init__(self,name, staffNo):
        self._name = name #private attribute
        self.staffNo = staffNo #public
        
        
    def showDetails(self):
        print("Employee Name: ", self.name)
        print("Employee Number: ", self.staffNo)
        
myStaff = employee("Eric Jones", 7878)

    
        
    