# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:04:58 2022

@author: suman
"""
#to check given binary tree is complete binary tree or not
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right =None
        
def Inorder(node):
    if node is None:
        return 0
    Inorder(node.left)
    print(node.data,end=" ")
    Inorder(node.right)
    
def depth(node):
    d=0
    while(node!=None):
        d+=1
        node = node.left
    return d
def  completerec(node,d,level=0):
    if node is None:
        return True
    if node.left == None and node.right == None:
        return (d == level+1)
    if node.left == None or node.right == None:
        return False
    return completerec(node.left, d,level+1) and completerec(node.right, d,level+1)

def complete_binary(node):
    d = depth(node)
    return completerec(node, d)


    
if __name__ == '__main__':
    
    root = Node(4)
    root.left = Node(5)
    root.right = Node(7)
    root.left.left = Node(13)
    root.left.right = Node(15)
    root.right.left = Node(19)
    root.right.right = Node(27)
    
    Inorder(root)
    if(complete_binary(root) == True):
        print("\nThe given binary is complete Binary tree")
    else:
        print("\nThe given binary is not complete Binary tree")