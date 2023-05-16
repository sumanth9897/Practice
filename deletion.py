# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:46:14 2023

@author: suman
"""

class Node:
    def __init__(self,data):
        self.right = None
        self.data = data 
        self.left = None
        
def Inorder(node):
    if node is None:
        return 
    Inorder(node.left)
    print(node.data,end =" ")
    Inorder(node.right)
    
def Search(node,key):
    if node is None or node.data == key:
        return node
    elif(key < node.data):
        return Search(node.left,key)
    else:
        return Search(node.right,key)
    


if __name__ = '__main__':
    
    
    
