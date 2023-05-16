# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:51:33 2022

@author: suman
"""

#creation of singly linkedlist 
#creation of node 
class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

#creation of linkedlist
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        temp = self.head 
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
            
#code exection starts here
if __name__ == '__main__':
    
    Nlist = Linkedlist()
    
    Nlist.head = Node(5)
    s2 = Node(6)
    s3 = Node(9)
    
    Nlist.head.next = s2
    s2.next = s3
    
    Nlist.printlist()