# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:06:13 2024

@author: Support
"""

class TstudentRecord:
    def __init__(self,name, adress, className):
        self.name = name
        self.adress = adress
        self.className = className
        
def appendRecord():
    terminator = 200
    fileName = "StudentRecord.txt"
    file  = open(fileName, 'w')
    while terminator != -1:
        terminator = int(input("Do you wish to exit, press -1 "))
        if terminator == -1:
            break
        else:
        
            name = input("Enter your name ")
            adress = input("Enter your adress ")
            className = input("Enter your class name ")
            string1 = name +"_"+adress +"_" + className
            file.writelines(string1 + "\n")
    file.close()
appendRecord()   
    