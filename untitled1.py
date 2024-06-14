# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:43:48 2023

@author: Support
"""

Temperature = [4,8,21,13,12,6,5,3,1,0]
First = 0
Last = 9
swap = False
while swap== False and Last>=0:
    swap = False
    for i in range(9):
        if Temperature[i]> Temperature[i+1]:
            temp = Temperature[i]
            Temperature[i] = Temperature[i+1]
            Temperature[i+1]= temp
            swap = True
    Last = Last - 1
    
print(Temperature)