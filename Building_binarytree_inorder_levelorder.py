# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:56:42 2022

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
    

def construct_tree(levelorder,inorder):
    if inorder:
        for i in range(0,len(levelorder)):
            if levelorder[i]  in inorder:
                node = Node(levelorder[i])
                node_index = inorder.index(levelorder[i])
                break
        node.left = construct_tree(levelorder,inorder[:node_index])
        node.right = construct_tree(levelorder,inorder[node_index +1 :])
        return node
       

inorder = ['D', 'B', 'E', 'A', 'F', 'C']
levelorder = ['A', 'B', 'C', 'D', 'E', 'F']
Inorder(construct_tree(levelorder, inorder))
