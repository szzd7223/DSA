from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs_traversal(root):
    if not root:
        return []

    queue = deque()
    queue.append(root)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Example usage:
if __name__ == "__main__":
    # Creating the tree:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("BFS Traversal:", bfs_traversal(root))
