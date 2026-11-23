# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l = []
        self.result = 0
        def fn(node, k):
            if not node or self.result:
                return
            fn(node.left, k)
            self.l.append(node.val)
            if len(self.l) == k:
                self.result = self.l[-1]
                return

            fn(node.right, k)
        fn(root, k)
        return self.result
       
        