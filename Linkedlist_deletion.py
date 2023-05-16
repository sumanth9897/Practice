# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:03:32 2022

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
    def deletion_from_front(self):
        temp = self.head 
        self.head = temp.next
        temp.next = None
    def deletion_from_end(self):
        temp = self.head
        while(temp.next):
            prev = temp 
            temp = temp.next
        prev.next = None
    
    def deletion_of_key(self,key):
        temp = self.head 
        if(temp!= None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
        while(temp!= None):
            if(temp.data == key):
                break
            prev = temp 
            temp = temp.next
            
        prev.next = temp.next
        temp = None
        
            
            
if __name__ == '__main__':
    
    L = Llists()
    
    L.head = Node(4)
    s2 = Node(5)
    s3 = Node(7)
    s4 = Node(8)
    
    L.head.next = s2
    s2.next = s3
    s3.next = s4

    L.Print()
    # print("\n")
    # L.deletion_from_front()
    # L.Print()
    # print("\n")
    # L.deletion_from_front()
    # L.Print()
    # print("\n")
    # L.deletion_from_end()
    # L.Print()
    print("\n")
    L.deletion_of_key(7)
    L.Print()
    