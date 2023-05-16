# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 20:16:07 2022

@author: suman
"""

class Listnode:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Treenode:
    def __init__(self,val):
        self.left = None
        self.val = val
        self.right = None
        
class convertion:
    
    def __init__(self):
        self.head = None
        self.root = None
        
    def push(self,data):
        
        new_node = Listnode(data)
        
        new_node.next = self.head 
        
        self.head = new_node
        
    def convert_list_to_binary(self):
        
        q=[]
        
        if self.head is None:
            self.root = None
            return
        
        self.root = Treenode(self.head.data)
        q.append(self.root)
        self.head = self.head.next
        
        while(self.head):
            
            temp = q.pop(0)
            lchild = None
            rchild = None
            
            lchild = Treenode(self.head.data)
            q.append(lchild)
            self.head = self.head.next
            if(self.head):
                rchild = Treenode(self.head.data)
                q.append(rchild)
                self.head = self.head.next
                
            temp.left = lchild
            temp.right = rchild
        
    def Inorder(self,node):
        if node is None:
            return 0
        self.Inorder(node.left)
        print(node.val,end=" ")
        self.Inorder(node.right)
        


    

    
if __name__ == '__main__':
    
    ob1 = convertion()
    
    ob1.push(36)
    ob1.push(30)
    ob1.push(25)
    ob1.push(15)
    ob1.push(12)
    ob1.push(10)
    
    ob1.convert_list_to_binary()
    
    print("Inorder traversal of binary tree:")
    ob1.Inorder(ob1.root)
    
        
        
        
        
        
        
        
        
        
        
        