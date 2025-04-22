class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    # If tree is empty, it's symmetric
    if not root:
        return True

    # A helper function to compare two nodes
    def isMirror(t1, t2):
        # Both nodes are empty → mirror
        if not t1 and not t2:
            return True
        # One is empty, one is not → not mirror
        if not t1 or not t2:
            return False
        # Check current values and mirror children
        return (t1.val == t2.val and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left))

    return isMirror(root.left, root.right)
