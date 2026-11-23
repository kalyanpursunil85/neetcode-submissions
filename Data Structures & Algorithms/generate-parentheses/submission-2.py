class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        currState, condition, constraint
        """
        l, r = 0, 0 
        result = []

        def backtrack(currState, l, r):

            if l == r == n:
                result.append("".join(currState))
                return
            if l < n:
                currState.append("(")
                backtrack(currState, l+1, r)
                currState.pop()
            
            if r < l:
                currState.append(")")
                backtrack(currState, l, r+1)
                currState.pop()
        
        backtrack([], 0, 0)
        return result


