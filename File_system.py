class FileNode:
    def __init__(self, name, is_folder):
        self.name = name
        self.is_folder = is_folder
        self.left = None
        self.right = None

# Example Usage
root = FileNode("root", True)
root.left = FileNode("folder1", True)
root.right = FileNode("folder2", True)
root.left.left = FileNode("file1.txt", False)
root.left.right = FileNode("file2.txt", False)

# Function to print the file system
def print_file_system(node, indent=0):
    if node:
        print("  " * indent + node.name)
        print_file_system(node.left, indent + 1)
        print_file_system(node.right, indent + 1)

print_file_system(root)
