#Binary Tree Level Order Traversal - BFS - Leetcode 102
from typing import List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res


tree = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15,TreeNode(1,TreeNode(7),TreeNode(8)),TreeNode(7))))
s = Solution()
solution = s.levelOrder(tree)
print(solution)