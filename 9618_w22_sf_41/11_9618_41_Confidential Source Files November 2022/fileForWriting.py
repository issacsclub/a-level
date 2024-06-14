# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:55:31 2024

@author: Support
"""

fileName= "newtxt.txt"

file = open(fileName,'w')
for i in range(3):
    number = input("Enter a number ")
    file.write(number + '\n')
    
file.close()