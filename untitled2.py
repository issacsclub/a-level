# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:54:40 2023

@author: Support
"""

Temperature = [4,8,21,13,12,6,5,3,1,0]
First = 0
Last = 9
swap = False
for j in range(10):
    for i in range(9):
        if Temperature[i]> Temperature[i+1]:
            temp = Temperature[i]
            Temperature[i] = Temperature[i+1]
            Temperature[i+1]= temp
            swap = True
 
    
print(Temperature)