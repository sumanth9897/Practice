# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:27:25 2022

@author: suman
"""

#detecting a loop in the linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def Append(self,new):
        temp = self.head 
        new_node = Node(new)
        if temp is None :
            self.head = new_node
            return
        while(temp.next):
            temp = temp.next 
        temp.next = new_node
        
    def display(self):
        temp = self.head 
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next
    
    def push(self,new):
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head 
        self.head = new_node
        
    def Detect_loop(self,llist):
        slowptr = llist.head
        fastptr = llist.head
        while(fastptr.next != None and fastptr.next.next !=None):
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            if (slowptr == fastptr):
                return True
        return False
    
if __name__ == '__main__':
    
    L = Linkedlist()
    
    L.push(5)
    L.Append(4)
    L.Append(23)
    L.Append(54)
    
    L.display()
    #creating a loop
    L.head.next.next = L.head
    if(L.Detect_loop(L) == True):
        print("Loop detected")
    else:
        print("loop not detected")
        