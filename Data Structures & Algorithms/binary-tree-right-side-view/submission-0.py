# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        def fn(node, depth):
            if not node:
                return
            
            if len(self.result) == depth:
                self.result.append(node.val)
            fn(node.right, depth+1)
            fn(node.left, depth+1)
        
        fn(root, 0)
        return self.result