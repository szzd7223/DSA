class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root is None:
        return []
    
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

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

    print("Pre-order Traversal:", preorder_traversal(root))
