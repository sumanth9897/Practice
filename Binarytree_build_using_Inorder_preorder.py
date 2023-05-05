# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 12:34:16 2022

@author: suman
"""

class  Node:
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
    

def construct_tree(preorder,inorder):
    if inorder:
        root = Node(preorder.pop(0))
        root_index = inorder.index(root.data)
        #print(root_index,root.data)
        root.left = construct_tree(preorder, inorder[:root_index])
        root.right = construct_tree(preorder, inorder[root_index+1:])
        return root

inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
Inorder(construct_tree(preorder, inorder))



    
        