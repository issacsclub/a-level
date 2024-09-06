# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:15:50 2024

@author: Support
"""

class Card:
    def __init__(self, Number, Colour):
        #Colour:STRING
        #Number: INTEGER
        self.__Number = Number
        self.__Colour = Colour
        
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
    
    # (iii)
OneRed = Card(1,"Red")
TwoRed = Card(2,"Red")
ThreeRed = Card(3,"Red")
FourRed = Card(4,"Red")
FiveRed = Card(5,"Red")
OneBlue = Card(1,"Blue")
TwoBlue  = Card(2,"Blue")
ThreeBlue = Card(3,"Blue")
FourBlue  = Card(4,"Blue")
FiveBlue  = Card(5,"Blue")
OneYellow = Card(1,"Yellow")
TwoYellow = Card(2,"Yellow")
ThreeYellow = Card(3,"Yellow")
FourYellow = Card(4,"Yellow")
FiveYellow = Card(5,"Yellow")

# b (i)
class Hand:
    def __init__(self,Card1,Card2, Card3, Card4, Card5):
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = 0
        self.__NumberCards = 5
     # b(ii) 
    def GetCard(self, index):
        return self.__Cards[index]
    
Player1 = Hand(OneRed,TwoRed,ThreeRed,FourRed,OneYellow)
Player2 = Hand(TwoYellow,ThreeYellow,FourYellow,FiveYellow,OneBlue)

#C
def Calculate(Player):
    score = 0
    for i in range(5):
        CardGot = Player.GetCard(i)
        score = score + CardGot.GetNumber()
        color = CardGot.GetColour
        if color=="Red":
            score = score + 5  
        elif color == "Blue":
            score = score + 10
        else:
            score = score + 15
    return score

player1Points= Calculate(Player1)
player2Points= Calculate(Player2)

if player1Points > player2Points:
    print("PLayer 1 wins")
elif player2Points > player1Points:
    print("Player 2 wins")
else:
    print("It's a draw ")
    
        
    


    
    