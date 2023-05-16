# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:07:44 2022

@author: suman
"""

#insertion in linked list 
#insertion at front of linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    
    def __init__(self):
        self.head = None
        
    def Printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            
            temp = temp.next
    def insertion_in_front(self,new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node

if __name__ == '__main__':
    
    Linklist = Linkedlist()
    
    Linklist.head = Node(3)
    s2 = Node(6)
    s3 = Node(8)
    s4 = Node(9)
    
    Linklist.head.next = s2
    s2.next = s3
    s3.next =s4
    
    Linklist.Printlist()
    Linklist.insertion_in_front(10)
    print("\nlinked list after insertion from the front")
    Linklist.Printlist()
    
        