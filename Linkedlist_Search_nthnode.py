# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 10:26:04 2022

@author: suman
"""
#function to get the Nth node in linked list
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
            
    def Search_nTh(self,index):
        temp = self.head 
        count = 0
        
        while(temp):
            if(count == index):
                print("\nThe value at given index is :",temp.data)
            count +=1
            temp = temp.next
    


				
        				 

					
					
				
					

			
            
if __name__ == '__main__':
    
    L = Linkedlist()
    
    L.push(5)
    L.Append(4)
    L.Append(23)
    L.Append(54)
    L.Append(76)
    L.push(29)
    L.push(99)
    L.Append(4)
    L.Append(54)
    L.display()
    
    
    L.Search_nTh(0)
    
    L.display()
    
    
    
        
        
        