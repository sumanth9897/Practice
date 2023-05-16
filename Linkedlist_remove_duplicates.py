# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:00:28 2022

@author: suman
"""
#removing duplicates from the linked list
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
        
    def remove_duplicates(self):
        ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head
        while (ptr1 != None and ptr1.next != None):
            ptr2 = ptr1
            while (ptr2.next != None):
                if (ptr1.data == ptr2.next.data):
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                    dup.next = None
                else:
                    ptr2 = ptr2.next
                    
            ptr1 = ptr1.next
    
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
    print("linked list before removing duplicates:",end =" ")
    L.display()
    print("\nlinked list after removing linkedlist :",end = " ")
    L.remove_duplicates()
    L.display()