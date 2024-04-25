# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isEvenOddTree( root) -> bool:
        level=0
        curlevel=[root]
        nextlevel=[]
        while curlevel:
            for i in range(len(curlevel)):
                curr=curlevel[i]
                if curr.left:
                    nextlevel.append(curr.left)
                if curr.right:
                    nextlevel.append(curr.right)
                if curr.value % 2==level%2:
                    return False
                if i>0 and level%2==0 and curr.value<=curlevel[i-1].value:
                    return False
                if i>0 and level%2!=0 and curr.value>=curlevel[i-1].value:
                    return False
            curlevel=nextlevel
            nextlevel=[]
            level+=1
        return True


s = Solution()
print(s.isEvenOddTree(TreeNode(1, TreeNode(10, TreeNode(3), TreeNode(12)), TreeNode(2, TreeNode(9), TreeNode(13)))))
print(s.isEvenOddTree(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(14), TreeNode(10)), TreeNode(7, TreeNode(13), TreeNode(12))), TreeNode(8, TreeNode(15), TreeNode(6)))))
print(s.isEvenOddTree(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6, TreeNode(7)))))))))
print(s.isEvenOddTree(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(14), TreeNode(10)), TreeNode(7, TreeNode(13), TreeNode(12))), TreeNode(8, TreeNode(15), TreeNode(6)))))
print(s.isEvenOddTree(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6, TreeNode(7)))))))))
