class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insertRecursive(self, data, node):
        if node == None:
            return Node(data)
        elif data > node.data:
            node.right = self.insertRecursive(data, node.right)
        elif data < node.data:
            node.left = self.insertRecursive(data, node.left)
        return node
    
    def insert(self, data):
        self.root = self.insertRecursive(data, self.root)