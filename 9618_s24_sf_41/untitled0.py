# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 08:17:44 2024

@author: Support
"""
array = []
text = "we, are, the, world, we, are, the, children"


for i in text:
    array.append(i.split(","))
    
    
print(array[0])