class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root is None:
        return []
    
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Example usage:
if __name__ == "__main__":
    # Tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("In-order Traversal:", inorder_traversal(root))
