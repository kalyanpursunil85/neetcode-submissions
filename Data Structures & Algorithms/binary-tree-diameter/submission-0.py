# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def fn(node):
            if not node: return 0
            left = fn(node.left)
            right = fn(node.right)
            self.result = max(self.result, left+right)
            return 1 + max(left, right)
        fn(root)
        return self.result
