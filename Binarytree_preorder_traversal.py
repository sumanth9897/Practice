#preorder traversal without using recursion
class  Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
         
def preorder(node):
    
    if node is None:
        return 
    
    stack =[]
    stack.append(node)
    
    while(len(stack)>0):
        
        node = stack.pop()
        print(node.data,end =" ")
        
        if (node.right is not None):
            stack.append(node.right)
            
        if (node.left is not None):
            stack.append(node.left)
            
if __name__  == '__main__':
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.left.left = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("preorder traversal of binary tree:")
    preorder(root)