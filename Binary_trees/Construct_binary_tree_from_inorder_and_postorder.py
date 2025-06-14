# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder, postorder):
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)

        root.right = buildTree(inorder[mid+1:], postorder)
        root.left = buildTree(inorder[:mid], postorder)

        return root

print(buildTree([9,3,15,20,7], [9,15,7,20,3]))