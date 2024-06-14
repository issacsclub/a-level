# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:35:11 2024

@author: Support
"""


dataArray = [None for i in range(100)]

def ReadFile():
    try:
        file = open("IntegerData.txt",'r')
        for i in range(100):
            dataArray[i] = int(file.readline())
        file.close()
    
    except:
        print("The file does not exist ")
        
        
def FindValues():
    
    numberOfTimes = 0
    while True:
        
        number = int(input("Enter a number between 0  and 100 "))
        if number>100 or number <0:
            print("invalid number")
        else:
            break
    for i in range(100):
        if dataArray[i] == number:
            numberOfTimes = numberOfTimes + 1
    return numberOfTimes
            
# d (i)
ReadFile()
print("The number appears ", FindValues(), "times")
    
    
        

        


