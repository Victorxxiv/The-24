class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Preorder Traversal: Root -> Left -> Right
def preorder_traversal(root):
    if root:
        print(root.value)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Inorder Traversal: Left -> Root -> Right
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)

# Postorder Traversal: Left -> Right -> Root
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value)

# Example Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder Traversal: ")
preorder_traversal(root)

print("\nInorder Traversal: ")
inorder_traversal(root)

print("\nPostorder Traversal: ")
postorder_traversal(root)