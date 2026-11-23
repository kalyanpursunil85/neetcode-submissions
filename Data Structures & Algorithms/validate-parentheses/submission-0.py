class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []

        for i, c in enumerate(s):
            if c in valid.values():
                stack.append(c)
            else:
                if stack:
                    if not valid[c] == stack.pop():
                        return False
                else:
                    return False
        
        return False if stack else True
