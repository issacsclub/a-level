# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 12:32:29 2025

@author: Support
"""

count = 0
number = 8000.0
while number != 9999.9:
    number = float(input("Enter a number "))
    if number > 100:
        count = count + 1
        
print("Numbers greater than 100 ", count-1)