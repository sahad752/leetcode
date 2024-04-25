class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = array_to_bst(nums[:mid])
    root.right = array_to_bst(nums[mid+1:])
    return root

def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)

root = array_to_bst([1, 2, 3, 4, 5])
inorder_traversal(root)