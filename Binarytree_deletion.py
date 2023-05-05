# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:40:59 2022

@author: suman
"""

#deleting a node in binary tree 
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
    
    
def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
 
# function to delete element in binary tree
 
 
def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        deleteDeepest(root, temp)
        key_node.data = x
    return root
                
if __name__ == '__main__':
    
    root = Node(4)
    root.left = Node(6)
    root.right = Node(8)
    root.left.left  = Node(9)
    root.left.right  = Node(10)
    root.right.right =Node(15)
    root.right.left  = Node(19)
    print("before deleting the node:")
    Inorder(root)
    print("\nafter deleting the node :")
    deletion(root, 9)
    Inorder(root)