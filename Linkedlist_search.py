# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 19:20:28 2022

@author: suman
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head 
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
        
    def append(self,new):
        new_node = Node(new)
        temp = self.head 
        if temp is None:
            self.head = new_node
            return
        while(temp.next):
            temp = temp.next
            
        temp.next = new_node
        new_node.next = None
        
    # def Search(self,key):
    #     temp = self.head 
    #     while(temp):
    #         if (temp.data == key):
    #             return True
    #         temp = temp.next
    #     return False
    def Search(self,M,key):
        if(not M):
            return False
        if(M.data==key):
            return True
        return self.Search(M.next,key)            
        

if __name__ == '__main__':
    
    M =Linkedlist()
    
    # M.append(4)
    # M.append(8)
    # M.append(10)
    # M.append(27)
    # M.append(78)
    x= int(input("enter the value : "))
    for i in range(0,x):
        M.append(int(input("enter the value in the node:")))
        
    M.display()
    y = int(input("enter the value want to search :"))
    #print(M.Search(y))
    print(M.Search(M.head,y))
    