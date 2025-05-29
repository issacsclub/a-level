# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:51:25 2025

@author: Support
"""

 #Python program for finding an item in a linked list
myLinkedList = [27, 19, 36, 42, 16, None, None, None, None, None, None, None]
myLinkedListPointers = [-1, 0, 1, 2, 3 ,6 ,7 ,8 ,9 ,10 ,11, -1]
startPointer = 4
nullPointer = -1
def find(itemSearch): 
   found = False
   itemPointer = startPointer
   while itemPointer != nullPointer and not found:
        if myLinkedList[itemPointer] == itemSearch:
           found = True
        else:
           itemPointer = myLinkedListPointers[itemPointer]
   return itemPointer
#enter item to search for
item = int(input("Please enter item to be found "))
result = find(item) 
if result != -1:
    print("Item found")
else:
    print("Item not found")
    
    
def insert(itemAdd):
    global startPointer
    if heapStartPointer == nullPointer:
       print("Linked List full")
    else:
       tempPointer = startPointer
       startPointer = heapStartPointer
       heapStartPointer = myLinkedListPointers[heapStartPointer]
       myLinkedList[startPointer] = itemAdd
       myLinkedListPointers[startPointer] = tempPointer