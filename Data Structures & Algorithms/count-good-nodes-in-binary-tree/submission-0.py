# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def fn(node, max_so_far):
            if not node:
                return 0
            
            self.good = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)
            self.good += fn(node.left, max_so_far)
            self.good += fn(node.right, max_so_far)
            return self.good
        
        fn(root, root.val)
        return self.good
