class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"{": "}", "[": "]", "(": ")" }
        closing = mapping.values()
        for c in s:
            if c not in closing:
                stack.append(c)
            else:
                if stack:
                    v = stack.pop()
                    if c != mapping[v]:
                        return False
                else:
                    return False

        return True if not stack else False


        