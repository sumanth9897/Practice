# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 18:50:52 2022

@author: suman
"""

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head 
        while(temp):
            print(temp.data,end = "\t")
            temp = temp.next
    
    def append(self,new):
        new_node = Node(new)
        temp = self.head 
        if(temp== None):
            self.head = new_node
            return
        while(temp.next):
            temp = temp.next 
        
        temp.next = new_node
        
    def length_rec(self,node):
        if(not node):
            return 0
        else:
            return 1 + self.length_rec(node.next)
        
    def Length(self):
        return self.length_rec(self.head)
    
if __name__ == "__main__":
    M = Linkedlist()
    
    x= int(input("enter the value "))
    for i in range(0,x):
        M.append(int(input("enter the value in the node:")))
        
    M.display()
    print("\nthe length of linkedlist:",M.Length())
    
        
    