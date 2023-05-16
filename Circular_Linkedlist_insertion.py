# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:50:19 2022

@author: suman
"""

#circular linked list insertion from begining,end,and at particular key
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class CLinkedlist:
    def __init__(self):
        self.head = None
        
    def addToEmpty(self, data):
        if (self.head != None):
            return self.head
        
        temp = Node(data)
        self.head = temp
        self.head.next = self.head
        return self.head
        
    def add_at_begin(self,new):
        if (self.head == None):
           return self.addToEmpty(new)
        temp = self.head 
        newnode = Node(new)
        newnode.next = temp.next
        temp.next = newnode
        return temp
    def traverse(self):
        if (self.head == None):
            print("List is empty")
            return
        temp = self.head.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head.next:
                break
            
if __name__ == '__main__':
    C = CLinkedlist()
    
    C.add_at_begin(12)
    C.add_at_begin(9)
    C.add_at_begin(6)
    C.add_at_begin(3)
    C.add_at_begin(1)
    print("Values present in linked list :",end = " ")
    C.traverse()
    