# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:25:48 2022

@author: suman
"""

#finding the middle node  of the linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Llists:
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
        
    def Length(self):
        temp = self.head 
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count
    
    def Middle_node(self,llist):
        temp = self.head 
        count = 0
        c = llist.Length()
        x = c//2
        while(temp):
            if(count == x):
                print(temp.data)
                break
            temp = temp.next 
            count +=1
    def Middle_node_withoutlistTraversal(self):
        slowptr = self.head 
        fastptr = self.head 
        
        if self.head is not None:
            while (fastptr is not None and fastptr.next is not None):
                fastptr = fastptr.next.next
                slowptr = slowptr.next 
            print(slowptr.data)
            
if __name__ == '__main__':
    
    K = Llists()
    
    x = int(input("enter the number of nodes:"))
    for i in range(0,x):
        K.push(int(input("enter the value of node:")))
    
    print("\nThe middle node of linked list is :",end = " ")
    # K.Middle_node(K)
    K.Middle_node_withoutlistTraversal()    
    