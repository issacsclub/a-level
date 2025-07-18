# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 08:56:23 2025

@author: Support
"""

class Horse:
    
    #Name : STRING
    #MaxFenceHeight : INTEGER
    #PercentageSuccess : INTEGER
    def __init__(self, Name, MaxFenceHeight, PercentageSuccess):
        self.__Name = Name
        self.__MaxFenceHeight = MaxFenceHeight
        self.__PercentageSuccess = PercentageSuccess
        
    def GetName(self):
        return self.__Name
    
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    
    
Horses = [Horse("",None,None) for i in range(2)]

Horses[0] = Horse("Beauty", 150, 72)
Horses[1] = Horse("Jet", 160, 65)
        
        
    
  
    