# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 20:27:02 2022

@author: suman
"""

#deletion in binary search tree
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
def delete(node,key):
    if node == None:
        return node
    
    elif(node.data < key):
        node.right = delete(node.right, key)
        
    elif(node.data > key):
        node.left = delete(node.left, key)
    
    else:
        if