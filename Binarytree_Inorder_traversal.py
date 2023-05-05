# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:33:24 2022

@author: suman
"""

#Inorder traversal  : Left root right
#preorder traversal : root left right
#postorder traversal: right left root


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
    
def Preorder(node):
    
    if node is None:
        return 0
    
    print(node.data,end =" ")
    Preorder(node.left)
    Preorder(node.right)
    
def Postorder(node):
    
    if node is None:
        return 0
    
    Postorder(node.right)
    Postorder(node.left)
    print(node.data,end = " ")
    
if __name__ == '__main__':
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("inorder traversal of given tree is :")
    Inorder(root)
    
    print("\npreorder traversal of given tree is : ")
    Preorder(root)
    
    print("\nPost order traversal of given tree is :")
    Postorder(root)
    