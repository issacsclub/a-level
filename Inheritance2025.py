# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 08:32:10 2025

@author: Support
"""

class employee:
    def __init__(self, name, staffNo):
        self.__name = name
        self.__staffNo = staffNo
        self.__fullTimeStaff = True
        
    def showDetails(self):
        print("Employee name", self.__name)
        print("Employee Staff No: ", self.__staffNo)
        
class partTime(employee):
    def __init__(self, name, staffNo):
        employee.__init__(self, name, staffNo)
        self.__fullTimeStaff = False
        self.__hoursWorked = 0
        
    def getHoursWorked(self):
        return (self.__hoursWorked)

class fullTime(employee):
    def __init__(self, name, staffNo):
        employee.__init__(self, name, staffNo)
        self.__fullTimeStaff = True
        self.__yearSalary = 0
        
    def getYearSalary(self):
        return (self.__yearSalary)    


permanentStaff = fullTime("Eric Jones", 72) 
permanentStaff.showDetails()

temporaryStaff = partTime("Alice Hue", 1017)
temporaryStaff.showDetails()
                          