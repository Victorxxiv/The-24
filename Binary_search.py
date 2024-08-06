class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = BSTNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = BSTNode(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self._search(root.left, key)
        return self._search(root.right, key)

# Example Usage
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(6)
bst.insert(15)

print("Search for 15:", bst.search(15))
print("Search for 25:", bst.search(25))
