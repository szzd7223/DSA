class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder_traversal(root):
    if root is None:
        return []
    
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

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

    print("Post-order Traversal:", postorder_traversal(root))
