# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 09:39:20 2025

@author: Support
"""

NumberArray = [100,85,644, 22, 15,8,1]


def RecursiveInsertion(IntegerArray,NumberElements):
    
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements-1)
        LastItem = IntegerArray[NumberElements-1]
        CheckItem = NumberElements-2
    LoopAgain = True    
    if CheckItem < 0:
        LoopAgain= False
    elif IntegerArray[CheckItem] < LastItem:
        LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem -1
        if CheckItem <0:
            LoopAgain  = False
        elif IntegerArray[CheckItem + 1] == LastItem:
            LoopAgain = False
        
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray
        
#RecursiveInsertion(NumberArray,7)

def IterativeInsertion(IntegerArray,NumberElements):
    
    while NumberElements >0:
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
        LoopAgain = True
        if CheckItem <0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
        while LoopAgain:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem = CheckItem -1
            if CheckItem <0:
                LoopAgain  = False
            elif IntegerArray[CheckItem + 1] == LastItem:
                LoopAgain = False
            IntegerArray[CheckItem + 1] = LastItem
            NumberElements = NumberElements - 1
        
    
    return IntegerArray
IterativeInsertion(NumberArray,7)