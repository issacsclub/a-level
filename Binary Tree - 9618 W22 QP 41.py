# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:05:24 2024

@author: Support
"""

ArrayNodes = [[-1,-1,-1] for i in range(20)]

for i in range(6):
    print("Row ", i)
    x = int(input("Insert left pointer "))
    y = int(input("Insert data item "))
    z = int(input("Insert right pointer "))
    
    ArrayNodes[i] = [x,y,z]

print(ArrayNodes)

FreeNode = 6
RootPointer  = 0


def SearchValue(Root, ValueToFind):
    if Root == -1:
        return -1
    else:
        