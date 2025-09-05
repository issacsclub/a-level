# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 16:12:09 2025

@author: Support
"""

DataArray = [None for i in range(100)]

def ReadFile():
    
    global DataArray
    
    try:
        fileName = "IntegerData.txt"
        File = open(fileName,'r')
        for i in range(100):
            DataArray[i] = int(File.readline())            
        File.close()
    except IOError:
        print("File not found")
        
def FindValues():
    
    number = 150
    while number <1 or number>100:
        number = int(input("Enter a number between 1 and 100 "))
    
    count = 0
    for i in range(100):
        if DataArray[i]== number:
            count = count + 1
    return count 
ReadFile()


print("the number appears ", FindValues(), " times ")

    
    