# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 08:35:05 2024

@author: Support
"""

class Tree:
    
    def __init__(self, TreeName, HeightGrowth, MaxHeight, MaxWidth,Evergreen):
        #Declare TreeName, Evergreen
        self.__TreeName = TreeName
        self.__HeightGrowth = HeightGrowth
        self.__MaxHeight = MaxHeight
        self.__MaxWidth = MaxWidth
        self.__Evergreen = Evergreen
    def GetTreeName(self):
        return self.__TreeName
    
    def GetGrowth(self):
        return self.__HeightGrowth


def ReadData():
    TreeData= []
    FileName = "Trees.txt"
    Array2 = []
    try:
        File = open(FileName, 'r')
        for i in range(9):
            
            Array2.append(File.readline().split(","))
            
    except:
        print("no such file ")
    
        
        
ReadData()
            
    