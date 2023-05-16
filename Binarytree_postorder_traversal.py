#postorder traversal 
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
def postorder(node):
    if node is None:
        return
    
    stack1 =[]
    stack2 =[]
    stack1.append(node)
    
    while(stack1):
        
        node = stack1.pop()
        stack2.append(node)
           
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)
            
    while (stack2):
        node = stack2.pop()
        print(node.data,end =" ")
        
            

if __name__ == '__main__':
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.left.left = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("post order traversal :")
    postorder(root) 