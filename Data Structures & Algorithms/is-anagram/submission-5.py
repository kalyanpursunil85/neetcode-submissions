class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        from collections import Counter
        
        x, y = Counter(s), Counter(t)
        return x == y

