# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 10:46:34 2022

@author: suman
"""

#function to get nth node using recursion 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def push(self,new):
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head 
        self.head = new_node
        
    def display(self):
        temp = self.head 
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next
            
        
    def Append(self,new):
        new_node = Node(new)
        temp = self.head
        if temp is None :
            self.head = new_node
            return
        while(temp.next):
            temp = temp.next 
        
        temp.next = new_node
        
    def getnth(self,llist,position):
         llist.getnthnode(self.head,position,llist)
    
    def getnthnode(self,head,position,llist):
        count = 0
        if(head):
            if count == position:
                print(head.data)
            else:
                llist.getnthnode(head.next,position-1,llist)
        else:
            print("index does not exist")

if __name__ == '__main__':
    
    L = Linkedlist()
    
    L.push(5)
    L.Append(4)
    L.Append(23)
    L.Append(54)
    L.Append(76)
    L.push(29)
    L.push(99)
    L.display()
    print("\nthe value at index 3 is : ",end = " ")
    
    L.getnth(L, 3)