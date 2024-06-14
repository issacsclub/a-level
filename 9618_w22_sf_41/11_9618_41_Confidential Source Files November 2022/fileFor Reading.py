# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:00:58 2024

@author: Support
"""

fileName = "newtxt.txt"
dataArray = [None for i in range(3)]

file = open(fileName,'r')

for i in range(3):
    dataArray[i] = int(file.readline())
    
file.close()

print(dataArray)
    

