# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q: return True
            if p and not q: return False
            if q and not p: return False
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        def fn(node, subRoot):
            if not node: return False
            if isSameTree(node, subRoot): 
                return True
            
            return fn(node.left, subRoot) or fn(node.right, subRoot)
        
        return fn(root, subRoot)