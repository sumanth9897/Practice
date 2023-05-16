# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:20:00 2022

@author: suman
"""

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        
class Llists:
    
    def __init__(self):
        self.head = None
        
    def Print(self):
        temp = self.head 
        while(temp):
            print(temp.data,end="\t")
            temp =temp.next
    
    def insertion_in_front(self,new):
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
            
    def Insertion_at_Last(self,new):
        
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head 
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        
    def Insertion_after(self,prev,nod):
        
        new_node = Node(nod)
        if (prev ==self.head):
            self.head.next = new_node
            return
        temp = self.head 
        while(temp!= prev):
            temp = temp.next 
        new_node.next = temp.next 
        temp.next = new_node

if __name__ == '__main__':
    
    L = Llists()
    
    L.head = Node(4)
    s2 = Node(5)
    s3 = Node(7)
    s4 = Node(8)
    
    L.head.next = s2
    s2.next = s3
    s3.next = s4
    
    
    L.insertion_in_front(9)
    
    
    print("linked list before insertion :")
    L.Print()
    L.Insertion_at_Last(19)
    print("\nlinked list after insertion :")
    L.Print()
    print("\nlinked list after in insertion between certain node :")
    L.Insertion_after(s2, 34)
    L.Print()
    
         
    
        
        