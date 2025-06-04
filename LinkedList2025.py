# -*- coding: utf-8 -*-
"""
Created on Fri May 30 09:57:50 2025

@author: Support
"""

# Simulated linked list using arrays
myLinkedList = [None] * 12
myLinkedListPointers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1]
startPointer = -1
nullPointer = -1
heapStartPointer = 0

def find(itemSearch): 
    found = False
    itemPointer = startPointer
    while itemPointer != nullPointer and not found:
        if myLinkedList[itemPointer] == itemSearch:
            found = True
        else:
            itemPointer = myLinkedListPointers[itemPointer]
    return itemPointer if found else -1

def insert(itemAdd):
    global startPointer, heapStartPointer
    if heapStartPointer == nullPointer:
        print("Linked List full")
    else:
        newNodePointer = heapStartPointer
        heapStartPointer = myLinkedListPointers[heapStartPointer]
        myLinkedList[newNodePointer] = itemAdd
        myLinkedListPointers[newNodePointer] = startPointer
        startPointer = newNodePointer

def delete(itemDelete):
    global startPointer, heapStartPointer
    currentPointer = startPointer
    previousPointer = nullPointer
    found = False

    while currentPointer != nullPointer and not found:
        if myLinkedList[currentPointer] == itemDelete:
            found = True
        else:
            previousPointer = currentPointer
            currentPointer = myLinkedListPointers[currentPointer]

    if not found:
        print("Item not found in the list.")
        return

    # Remove node from the linked list
    if previousPointer == nullPointer:
        # Deleting the first node
        startPointer = myLinkedListPointers[currentPointer]
    else:
        myLinkedListPointers[previousPointer] = myLinkedListPointers[currentPointer]

    # Add the node back to the free list
    myLinkedListPointers[currentPointer] = heapStartPointer
    heapStartPointer = currentPointer
    myLinkedList[currentPointer] = None
    print(f"Item {itemDelete} deleted.")

# --- Example usage ---
insert(10)
insert(20)
insert(30)

print("Initial list:")
print(myLinkedList)
print(myLinkedListPointers)

item = int(input("Enter item to delete: "))
delete(item)

print("List after deletion:")
print(myLinkedList)
print(myLinkedListPointers)

searchItem = int(input("Enter item to find: "))
result = find(searchItem)
if result != -1:
    print(f"Item found at index {result}")
else:
    print("Item not found")
