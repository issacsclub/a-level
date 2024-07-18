# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 09:14:18 2024

@author: Support
"""

DataArray = [9,3,5,1,2,13,6,10,11,12]

swap = True

top = len(DataArray)

while swap == True or top > 0:
    swap = False
    for index in range(top-1):
        if DataArray[index] > DataArray[index+1]:
            temp = DataArray[index]
            DataArray[index] = DataArray[index+1]
            DataArray[index+1] = temp
            swap = True
    top = top - 1
print(DataArray)