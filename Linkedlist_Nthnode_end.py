# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:05:19 2022

@author: suman
"""
#program for nth node from the end of the linkedlist
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
    def push(self,new):
        newnode = Node(new)
        if self.head is None:
            self.head = newnode
            return
        newnode.next = self.head 
        self.head = newnode
    
    def Append(self,new):
        newnode = Node(new)
        temp = self.head 
        if self.head is None:
            self.head = newnode
            return
        while(temp.next):
            temp = temp.next 
        temp.next = newnode
        
    def Length(self):
        temp = self.head 
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count
            
    # def getnth_last(self,llist,index):
    #     c =llist.Length()
    #     N = c - index
    #     count = 0
    #     temp = self.head 
    #     while(temp):
    #         if(count == N):
    #             print(temp.data)
    #         count+=1
    #         temp = temp.next
    
    #insertion at the nth node from the end
    # def getnth_last(self,llist,index,new):
    #     c =llist.Length()
    #     N = c - index
    #     count = 0
    #     temp = self.head 
    #     new_node = Node(new)
    #     while(temp):
    #         if(count == N):
    #             new_node.next = temp.next 
    #             temp.next = new_node
    #             return
    #         count+=1
    #         temp = temp.next
    
    #deletion at the nth node from the end
    def delete_nth_last(self,llist,index):
        c =llist.Length()
        N = c - index
        count = 0
        temp = self.head 
        prev = None
        while(temp):
            if(count == N):
                prev.next = temp.next
                temp.next = None
                return
            
            count+=1
            prev = temp
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
    L.display()
    print("\nThe value of node which  index from last :",end =" ")
    # L.getnth_last(L,5)
    # L.getnth_last(L,5, 56)
    L.delete_nth_last(L,3)

    L.display()
    
        