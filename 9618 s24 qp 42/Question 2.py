# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 09:24:24 2025

@author: Support
"""

class Node:
    
    def __init__(self,Data):
        # Data, LeftPonter, RightPOinter: Integer
        self.Data = Data
        self.LeftPointer = -1
        self.RightPointer = -1
        
    def GetLeft(self):
        return self.LeftPointer
    
    def GetRight(self):
        return self.RightPointer
    
    def GetData(self):
        return self.Data
    
    def SetLeft(self, item):
        self.LeftPointer = item


    def SetRight(self, item):
        self.RightPointer = item

    def SetData(self, item):
        self.Data= item
        
class TreeClass:
    
    def __init__(self):
        self.__Tree = [Node(-1) for i in range(20)] # Node
        self.__FirstNode = -1 # Integer
        self.__NumberNodes = 0 # integer
        
    
        
        
        
    
    
    
        
        
    
        
        