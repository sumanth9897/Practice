# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:32:43 2022

@author: suman
"""

#level order traversal 
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
def height(node):
    if node is None:
        return 0
    
    lheight = height(node.left)
    rheight = height(node.right)
    
    if(lheight > rheight):
        return lheight +1
    else:
        return rheight +1
    
def levelorder(node):
    h = height(node)
    for i in range(1,h+1):
        printlevel(node,i)
        
def printlevel(node,level):
    if node is None:
        return 
    if (level == 1):
        print(node.data,end=" ")
    else:
        printlevel(node.left, level-1)
        printlevel(node.right, level-1)
        
if __name__ == '__main__':
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("level order traversal :")
    levelorder(root)