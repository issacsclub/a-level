myLinkedList = [None for i in range(11)]
myLinkedListPointers = [None for i in range(11)]
heapStartPointer = 0
startPointer = -1
nullPointer = -1
for i in range(11):
    myLinkedListPointers[i] = i + 1
    
myLinkedListPointers[10] = -1


print("Pointers ", myLinkedListPointers)

print("Linked List ", myLinkedList)



# Adding items to a linked link

def LinkedListAdd(item):
    global heapStartPointer, startPointer
    # check if the list is full
    if heapStartPointer == nullPointer:
        print("Linked list is full")
        
    else:
        tempPointer = startPointer
        startPointer = heapStartPointer
        heapStartPointer = myLinkedListPointers[heapStartPointer]
        myLinkedList[startPointer] = item
        myLinkedListPointers[startPointer] = tempPointer
        
        return heapStartPointer, startPointer, nullPointer



    

