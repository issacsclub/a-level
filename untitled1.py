# -*- coding: utf-8 -*-
"""
Created on Tue May 13 15:40:58 2025

@author: Support
"""

Numbers = [45,8,3,1,5,10,56,11,18,9]
print("Before", Numbers)
lowerBound = 0
upperBound = 9
index = 0
swap = False
while swap==False or index <= upperBound:
    for count in range(9):
        if Numbers[count] > Numbers[count+1]:
            temp = Numbers[count]
            Numbers[count] = Numbers[count+1]
            Numbers[count+1] = temp
            swap = True
            
    index = index+1
         
print("After", Numbers)           
