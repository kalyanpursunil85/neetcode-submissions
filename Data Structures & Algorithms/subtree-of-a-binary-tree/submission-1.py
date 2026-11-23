# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_identical(p, q):
            if p and not q: return False
            if q and not p: return False
            if not p and not q: return True
            
            return p.val == q.val and is_identical(p.left, q.left) and is_identical(p.right, q.right)
        
        def fn(node, subRoot):
            if not node: return False
            if is_identical(node, subRoot):
                return True
            return fn(node.left, subRoot) or fn(node.right, subRoot)
        
        return fn(root, subRoot)

