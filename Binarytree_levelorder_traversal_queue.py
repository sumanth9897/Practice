#level  order traversal using queue
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        
def Levelorder(node):
    
    if node is None:
        return
    
    q =[]
    q.append(node)
    while(len(q)>0):
        
        
        print(q[0].data,end=" ")
        node = q.pop(0)
        
        if node.left is not None:
            q.append(node.left)
        
        if node.right is not None:
            q.append(node.right)
            
        
if __name__ == '__main__':
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.left.left = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("level order traversal of given tree :")
    Levelorder(root)