class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        # Recursively calculate the depth of the left and right subtrees
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        
        # Return the maximum of both subtrees' depths plus 1 for the current node
        return max(left_depth, right_depth) + 1
