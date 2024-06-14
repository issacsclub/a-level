# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:11:05 2024

@author: Support
"""
try:
    fileName = "fileB.txt"
    
    file = open(fileName,'r')
    file.close()
    
    
    except IOError:
    print("Oops! your file does not exist")