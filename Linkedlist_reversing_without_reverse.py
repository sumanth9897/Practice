# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:44:02 2022

@author: suman
"""

#reversing a linkedlist but not actually reversing it
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linked:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head 
        while(temp):
            print(temp.data,end =" ")
            temp = temp.next
            
    def push(self,new):
        newnode = Node(new)
        temp = self.head 
        if temp is None:
            self.head = newnode
            return
        newnode.next = self.head 
        self.head = newnode
    
    def Reversed(self,temp):
        
        if(temp):
            self.Reversed(temp.next)
            print(temp.data,end=" ")
        else:
            return
        
        
if __name__ == '__main__':
    
    K = Linked()
    
    x = int(input("enter the number of nodes:"))
    for i in range(0,x):
        K.push(int(input("enter the value of node:")))
        
    K.display()
    
    print("\nThe reverse  of linked list is :")
    K.Reversed(K.head)
    print("\n***********")
    K.display()