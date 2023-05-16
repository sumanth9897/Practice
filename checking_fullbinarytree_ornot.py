# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 16:42:38 2022

@author: suman
"""

#check if given binary tree is full binary tree or not
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right =None
        
def Full_binary(node):
    if node is None:
        return True
    
    if node.left is None and node.right is None:
        return True
    
    if node.left is not None and node.right is not None:
        return Full_binary(node.left) and Full_binary(node.right)
    
    return False

def Inorder(node):
    if node is None:
        return 0
    Inorder(node.left)
    print(node.data,end=" ")
    Inorder(node.right)
    
if __name__ == '__main__':
    
    root = Node(4)
    root.left = Node(5)
    root.right = Node(7)
    root.left.left = Node(13)
    root.left.right = Node(15)
    root.right.left = Node(19)
    root.right.right = Node(27)
    
    Inorder(root)
    if(Full_binary(root)==True):
        print("\nthe given binary tree is full binary tree")
    else:
        print("\nthe given binary tree is not full binary tree")