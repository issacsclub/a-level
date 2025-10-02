# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 08:13:56 2025

@author: Support
"""

class Horse:
    
    def __init__(self, Name, MaxFenceHeight,PercentageSuccess):
        # Name :  STRING
        # MaxFenceHeight, PercentageSuccess: INTEGER
        self.__Name = Name
        self.__MaxFenceHeight = MaxFenceHeight
        self.__PercentageSuccess = PercentageSuccess
        
        
    def GetName(self):
        return self.__Name
    
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    
    def Success(self, Height, Risk):
        if Height > self.__MaxFenceHeight:
            return self.__PercentageSuccess
        else:
            if Risk == 1:
                return self.__PercentageSuccess
            elif Risk==2:
                return self.__PercentageSuccess*0.9
            elif Risk==3:
                return self.__PercentageSuccess*0.8
            elif Risk==4:
                return self.__PercentageSuccess*0.7
            else:
                return self.__PercentageSuccess*0.6
            
    
    
Horses = [Horse("",None,None) for i in range(2)]
Horses[0] = Horse("Beauty",150,72)
Horses[1] = Horse("Jet",160,65)

print(Horses[0].GetName())
print(Horses[1].GetName())


class Fence:
    def __init__(self, Height, Risk):
        self.__Height = Height #Integer
        self.__Risk= Risk #Integer
        
    def GetHeight(self):
        return self.__Height
    
    def GetRisk(self):
        return self.__Risk
    
 

Course = []
for i in range(4):
    Valid = False
    while Valid == False:
        Height = int(input("Enter height in cm "))
        if Height >= 70 and Height <=180:
            Valid = True
    Valid = False
    while Valid == False:
        Risk = int(input("Enter the risk between 1 and 5"))
        if Risk >=1 and Risk <=5:
            Valid=True
            
    Course.append(Fence(Height,Risk))
    

# ... (previous code remains the same until the AverageSuccess loop)

AverageSuccess = []    
for i in range(2):
    Total = 0
    for j in range(4):
        chance = Horses[i].Success(Course[j].GetHeight(), Course[j].GetRisk())  # Use i for horse index
        print(Horses[i].GetName(), "Fence", j+1, "chance of success is ", chance, "%")  # Use i for horse index
        Total = Total + chance
    average = Total/4
    AverageSuccess.append(average)
    print(Horses[i].GetName(), " average success rate is ", average, "%")  # Use i for horse index

    
Highest= AverageSuccess[0]
Winner = -1
for i in range(2):
    if Highest < AverageSuccess[i]:
        Winner=i
        Highest = AverageSuccess[i]
print(Horses[Winner].GetName(), " has the highest average chance of success ")


        
        
        
    
        