# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:07:02 2022

@author: suman
"""

#creating a binary tree 
#creating a node 
#finding the height and diameter of the binary tree

class Node :
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
def height(node):
    
    if node is None :
        return 0
    
    return 1 +max(height(node.left),height(node.right))

def diameter(root):
    
    if root is None:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right) 
    
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
    
    return max(1+lheight+rheight, max(ldiameter,rdiameter))
        
if __name__ == '__main__':
    
    root = Node(4)
    root.left = Node(6)
    root.right = Node(8)
    root.left.left  = Node(9)
    root.left.right  = Node(10)
    root.right.right =Node(15)
    root.right.left  = Node(19)
    
    print(diameter(root))