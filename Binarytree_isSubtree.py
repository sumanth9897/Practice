# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 15:46:13 2022

@author: suman
"""

#check given tree is sub tree of the other tree or not
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
def IsIdentical(node1,node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    
    return(node1.data == node2.data and IsIdentical(node1.left, node2.left) and IsIdentical(node1.right, node2.right))

def IsSubtree(T1,T2):
    if T1 is None:
        return False
    if T2 is None:
        return True
    
    if(IsIdentical(T1, T2)):
        return True
    
    return IsSubtree(T1.left, T2) or IsSubtree(T1.right,T2)

if __name__ == '__main__':
    
    T1 = Node(10)
    T1.left = Node(12)
    T1.right = Node(13)
    T1.left.left = Node(15)
    T1.left.right = Node(17)
    T1.right.left = Node(19)
    T1.right.right = Node(23)
    T1.left.left.left = Node(27)
    T1.left.left.right = Node(31) 
    
    S1 = Node(12)
    S1.left = Node(15)
    S1.right = Node(17)
    S1.left.left = Node(27)
    S1.left.right = Node(31)
    

    if(IsSubtree(T1, S1)):
        print("The given tree is subtree ")
    else:
        print("The given tree is not a subtree")