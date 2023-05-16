# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:41:15 2022

@author: suman
"""

class Node:
    def __init__(self,data ):
        self.data = data
        self.next = None
        

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head 
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
            
    def Append(self,new):
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head 
        while(temp.next):
            temp = temp.next
        temp.next = new_node
            
    def reverse(self):
        prev = None
        curr = self.head 
        while(curr is not None):
            Y = curr.next
            curr.next = prev 
            prev = curr 
            curr = Y
        self.head = prev
        
if __name__ == '__main__':
    
    M = Linkedlist()
    
    x= int(input("enter the length of linkedlist:"))
    for i in range(0,x,1):
        M.Append(int(input("enter the value in the node:")))
        
    M.display()
    M.reverse()
    print("\nafter reversing the linkedlist")
    M.display()
    
    
    
        