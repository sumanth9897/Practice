# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:02:34 2022

@author: suman
"""

#creating a node for doubly linkedlist
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data 
        self.next = None
#creating a doubly linkedlist      
class DLinkedlist:
    def __init__(self):
        self.head = None
        
    def Append(self,new):
        new_node = Node(new)
        temp = self.head 
        if(temp is None):
            new_node.prev = None
            self.head = new_node
            return
            
        while(temp.next is not None):
            temp = temp.next 
            
        temp.next = new_node
        new_node.next = None
        
    def display(self):
        temp = self.head
        while(temp is not None):
            print(temp.data,end =" ")
            temp = temp.next
            
if __name__ =='__main__':
    
    M = DLinkedlist()
    
    x= int(input("enter number of nodes:"))
    for i in range(0,x):
        M.Append(int(input("enter the value in Node:")))
    M.display()
    
            
            