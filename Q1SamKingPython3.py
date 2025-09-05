# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 11:49:15 2025

@author: Support
"""

length = int(input("Enter length: "))
width = int(input("Enter width: "))
folded = int(input("Enter folds: "))
          
if folded == 0:
    area = length*width
    print(area)
else:
    area = length*width*folded*2
