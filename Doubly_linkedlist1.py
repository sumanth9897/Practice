#creation of doubly linked list and insertion 
#creation of node
class Node:
    def __init__(self,data):
        self.prev = None
        self.data =data
        self.next = None

#creation of double linkedlist
class DLlists:
    def __init__(self):
        self.head = None
    
    def display(self,node):
        
        while node:
            print(node.data,end = " ")
            node = node.next
            
    
 
        
    def push(self,new):
        temp = self.head
        new_node = Node(new)
        if temp is None:
            self.head = new_node
            self.head.prev = None
            self.head.next = None
            return
        temp.prev = new_node.next
        new_node.next = temp
        new_node.prev = None
        
        
if __name__ == '__main__':
    
    M = DLlists()
    
    x= int(input("enter the number of nodes :"))
    for i in range(0,x):
        M.push(input("enter the value of node :"))
        
    M.display(M.head)
