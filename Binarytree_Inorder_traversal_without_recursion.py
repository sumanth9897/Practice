# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 12:14:38 2022

@author: suman
"""

 #creating a binary tree and using inorder traversal to traverse the tree 
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
def Inorder(node):
    
    root = node
    stack = []
    while(True):
        
        if node is not None:
            stack.append(node)
            node = node.left
            
            
        elif(stack):
            node = stack.pop()
            print(node.data,end = " ")
            node = node.right
            
        else:
            break
        
        
if __name__ == '__main__':
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("inorder traversal of given tree:")
    
    Inorder(root)
            
            
            