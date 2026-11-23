class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l, r = 0, 0
        result = []
        stack = []
        def backtracking(l, r):
            # check if we reached the goal
            if l == r == n:
                result.append("".join(stack))
                return
            
            if l < n:
                stack.append("(")
                backtracking(l+1, r)
                stack.pop()

            if r < l:
                stack.append(")")
                backtracking(l, r+1)
                stack.pop()
        
        backtracking(0, 0)
        return result
        