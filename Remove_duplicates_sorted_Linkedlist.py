# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 10:47:50 2022

@author: suman
"""

#removing the duplicates from a sorted linked list 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def push(self,new):
        newnode = Node(new)
        newnode.next = self.head 
        self.head = newnode
        
    def display(self):
        temp = self.head 
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next
            
    def Remove_dup(self):
        ptr1 = self.head
        ptr2 = self.head.next 
        while(ptr2.next!= None):
            if(ptr1.data==ptr2.data):
                ptr1.next = ptr2.next
                ptr2 = ptr2.next
            else:
                ptr2 = ptr2.next
                ptr1 = ptr1.next 
        return self.head
if __name__ == '__main__': 
    M = Linkedlist()
    
    M.push(4)
    M.push(3)
    M.push(3)
    M.push(2)
    M.push(2)
    M.push(1)
    
    M.display()
    print("\nafter removing duplicates:")
    M.Remove_dup()
    M.display()
    
        
        