# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 09:06:04 2025

@author: Support
"""

class student:
    def __init__(self, name, DateOfBirth, examMark):
        self.__name = name
        self.__DateOfBirth = DateOfBirth
        self.__examMark = examMark
        
    def DisplayExamMark(self):
        print("Exam mark: ", self.__examMark)
        
myStudent = student("Joe", "20/10/2010", 45.8)
myStudent.DisplayExamMark()