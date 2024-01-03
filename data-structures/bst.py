class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.insertData(self.root, data)

    def insertData(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insertData(root.left, data)
        elif data > root.data:
            root.right = self.insertData(root.right, data)
        return root

    def search(self, data):
        return self.searchData(self.root, data)

    def searchData(self, root, data):
        if root is None or root.data == data:
            return root

        if data < root.data:
            return self.searchData(root.left, data)
        else:
            return self.searchData(root.right, data)

    def delete(self, data):
        self.root = self.deleteData(self.root, data)
    
    def deleteData(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.deleteData(root.left, data)
        elif data > root.data:
            root.right = self.deleteData(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.data = self.minValue(root.right).data
            root.right = self.deleteData(root.right, root.data)

        return root

    def minValue(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inOrderTraversal(self):
        return self.inOrder(self.root)

    def inOrder(self, root):
        result = []
        if root:
            result += self.inOrder(root.left)
            result.append(root.data)
            result += self.inOrder(root.right)
        return result

# Example Usage:
bst = BinarySearchTree()

nodes_to_insert = [50, 30, 70, 20, 40, 60, 80]
for node in nodes_to_insert:
    bst.insert(node)

print("In-order Traversal:", bst.inOrderTraversal())