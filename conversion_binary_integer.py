# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:54:26 2022

@author: suman
"""

#convert a binary number into integer
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def Length(self):
        temp = self.head 
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count
    
    # def conversion(self,llist):
    #     temp = self.head 
    #     if(temp is None):
    #         return None
    #     x = llist.Length()
    #     z=0
    #     for i in reversed(range(0,x)):
    #         c = temp.data
    #         f = 2**i
    #         y = c*f
    #         z+=y
    #         temp = temp.next
    #     return z
    def conversion(self,llist):
        result = 0
        temp = self.head
        while(temp):
            result = result*2 + temp.data
            temp = temp.next
        return result
    
    def push(self,new):
        newnode = Node(new)
        temp = self.head 
        if temp is None:
            self.head = newnode
            return
        newnode.next = self.head 
        self.head = newnode
    
if __name__ == '__main__':
    
    M = Linkedlist()
    
    x= int(input("enter the length of linkedlist:"))
    for i in range(0,x,1):
        M.push(int(input("enter the value in the node:"),2))
        
    print(M.conversion(M))