# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:23:02 2024

@author: Support
"""
Array = ["A", "C",  "B"]
DataArray = [None for i in range(25)]

fileName = "Data.txt"
try:
    file = open(fileName,'r')
    for i in range(25):
        DataArray[i] = int(file.readline())
    file.close()
    
except IOError:
    print("Oops! we cannot find the file you are looking for ")


def PrintArray(myArray):
    print(myArray)
    
    
PrintArray(DataArray)


def LinearSearch(myArray, SearchValue):
    index = 0
    times = 0
    while index < 25:
        if myArray[index] == SearchValue:
            times = times + 1 
        index = index + 1
        
    return times

print(LinearSearch(DataArray,7))
            

number = -1
while number < 0 or number > 100:
    number = int(input("Enter a number between 0 and 100 "))
print("The number ", number, "is found ", LinearSearch(DataArray,number ))   




