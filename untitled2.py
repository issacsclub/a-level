# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 09:11:01 2025

@author: Support
"""

def factorialIterative(number):
    if number == 0:
        answer = 1
    else:

        answer = 1
        for i in range(1, number+1):
            print("i", i)
            answer =  answer*i
            print("answere", answer)
            
    return answer

print(factorialIterative(0))
print(factorialIterative(5))
