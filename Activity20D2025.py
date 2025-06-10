# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 09:05:15 2025

@author: Support
"""

class student:
    
    def __init__(self, name, dateOfBirth, examMark):
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__examMark = examMark
        
    def displayMark(self):
        print("Student name: ", self.__name)
        print("Exam MArk ", self.__examMark)
        
class partTimeStudent(student):
    def __init__(self, name, dateOfBirth, examMark):
        student.__init__(self, name, dateOfBirth, examMark)
        self.__fullTimeStudent = False
        
        
        
class fullTimeStudent(student):
    def __init__(self, name, dateOfBirth, examMark):
        student.__init__(self, name, dateOfBirth, examMark)
        self.__fullTimeStudent = True
        
        
myFullTimestudent= fullTimeStudent("Mzomule", "20/01/2012", 65)
myFullTimestudent.displayMark()

myPartTimestudent= fullTimeStudent("Tawana", "20/01/2014", 55)
myPartTimestudent.displayMark()