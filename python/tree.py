#Binary Tree Level Order Traversal - BFS - Leetcode 102
from typing import List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    res = []

    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    inorder(root=root)
    return res

def inorder2(root):
    stack = []
    res = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr)
        curr = curr.right


if __name__ == "__main__":
    tree = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15,TreeNode(1,TreeNode(7),TreeNode(8)),TreeNode(7))))
    obj = inorderTraversal(tree)
    print(obj)