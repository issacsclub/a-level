# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:40:15 2025

@author: Support
"""

myFile = "myText.txt"

file=open(myFile, 'w')

textLine = "initial"

while textLine != "":
    textLine = input("Enter a line and press enter ")
    file.writelines(textLine + "\n")
    
file.close()

