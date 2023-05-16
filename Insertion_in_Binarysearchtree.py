# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 19:47:03 2022

@author: suman
"""

class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
def Inorder(node):
    if node is None:
        return 0
    Inorder(node.left)
    print(node.data,end = " ")
    Inorder(node.right)
    
def Search(node,key):
    
    if(node.data == key):
        return node
    
    if(node.data<key):
        return Search(node.right,key)
    
    Search(node.left,key)

def Insert(node,key):
    if node is None:
        return Node(key)
    else:
        if(node.data == key):
            return node
        elif(node.data<key):
            node.right = Insert(node.right,key)
            
        else:
            node.left = Insert(node.left,key)
    return node
if __name__ == '__main__':
    
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.left.right.left = Node(4)
    root.left.right.right =Node(7)
    
    Inorder(root)
    #x = int(input("enter the value to check in tree:"))
    #Search(root,x)
    Insert(root,12)
    print("\nAfter inserting the element in tree:")
    Inorder(root)
    