# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 12:31:41 2022

@author: suman
"""

#Addition of numbers in two linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = next 
        
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
    def Recursive_pair(self,h,llist):
        
        if( h == None and h.next == None):
            return
        else:
            temp = h.next
            h.next = temp.next
            temp.next = h
            temp = h
            
            h.next.next =  llist.Recursive_pair(h.next.next,llist)
            return h

if __name__ == '__main__':
    M = Linkedlist()
    
    M.push(4)
    M.push(3)
    M.push(3)
    M.push(2)
    M.push(2)
    M.push(1)
    
    M.display()
    M.Recursive_pair(M.head,M)

    M.display()