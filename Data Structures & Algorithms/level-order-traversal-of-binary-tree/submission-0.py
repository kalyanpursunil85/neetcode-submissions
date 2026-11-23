# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = defaultdict(list)

        def fn(node, level):
            if not node:
                return
            
            self.result[level].append(node.val)
            fn(node.left, level+1)
            fn(node.right, level+1)
        
        fn(root, 0)
        return [v for _, v in self.result.items()]
        
