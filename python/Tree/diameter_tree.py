# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.max_diameter =0
        def dfs(node):
            if not node:
                return 0
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            self.max_diameter = max(self.max_diameter,left_length+right_length)
            return 1+max(left_length,right_length)
        dfs(root)
        return self.max_diameter

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(s.diameterOfBinaryTree(root))
print(s.diameterOfBinaryTree(None))
print(s.diameterOfBinaryTree(TreeNode(1)))
print(s.diameterOfBinaryTree(TreeNode(1, TreeNode(2))))
print(s.diameterOfBinaryTree(TreeNode(1, TreeNode(2), TreeNode(3))))
print(s.diameterOfBinaryTree(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))))
print(s.diameterOfBinaryTree(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))))
print(s.diameterOfBinaryTree(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5), TreeNode(6)))))
