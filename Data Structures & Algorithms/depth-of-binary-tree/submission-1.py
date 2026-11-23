# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.result = 0
        def fn(node, depth):
            if not node:
                return 0
            self.result = max(self.result, depth)
            fn(node.left, depth+1)
            fn(node.right, depth+1)
        
        fn(root, 1)
        return self.result
        