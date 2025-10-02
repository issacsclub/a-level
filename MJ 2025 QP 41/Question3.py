# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 15:02:43 2025

@author: Support
"""

class Node:
    def __init__(self, NodeData):
        self.NodeData = NodeData  # DECLARE  NodeDAta: INTEGER
        self.LeftNode = None # DECLARE  LeftNode: INTEGER
        self.RightNode = None  # DECLARE  RightNode: INTEGER


    def GetLeft(self):
        return self.LeftNode
    
    def GetRight(self):
        return self.RightNode
    
    def GetData(self):
        return self.NodeData
    
    
    
    def SetLeft(self, Node):
        self.LeftNode = Node
        
    def SetRight(self, Node):
        self.RightNode = Node
        
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)

class Tree:
    def __init__(self,FirstNode):
        self.FirstNode = FirstNode # FirstNode: Node
    
    def GetRootNode(self):
        return self.FirstNode
    
    
    def Insert(self, NewNode):  
        CurrentNode = self.FirstNode  
        Inserted = True 
        while Inserted: 
            if NewNode.GetData() < CurrentNode.GetData():  
                if CurrentNode.GetLeft() == None: 
                    CurrentNode.SetLeft(NewNode)  
                    return True 
                else: 
                    CurrentNode = CurrentNode.GetLeft() 
            else: 
                if CurrentNode.GetRight() == None:  
                    CurrentNode.SetRight(NewNode)  
                    return True 
                else: 
                    CurrentNode = CurrentNode.GetRight() 
                    
                    

                
                
