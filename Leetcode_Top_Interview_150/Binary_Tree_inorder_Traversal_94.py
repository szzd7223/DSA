class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def Binary_Tree_Inorder_Traversal(root):
    res = []

    def dfs(node):
        if not node:
            return
        
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    
    dfs(root)

    return res

root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(5, TreeNode(6), TreeNode(7))

print(Binary_Tree_Inorder_Traversal(root))