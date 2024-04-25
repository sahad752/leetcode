# BFS algorithm for a tree in Python
import collections

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bfs_tree(root):
    if not root:
        return

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        currNode = queue.popleft()
        print("Visited", currNode.value, end=" ")

        if currNode.left and currNode.left not in visited:
            visited.add(currNode.left)
            queue.append(currNode.left)

        if currNode.right and currNode.right not in visited:
            visited.add(currNode.right)
            queue.append(currNode.right)



# Example tree
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# isEvenOddTree(root)
bfs_tree(root)